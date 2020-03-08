import asyncio
import logging

from apscheduler.jobstores.base import JobLookupError
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger

from piclodio3 import settings
from utils.player_manager import PlayerManager
from utils.singleton import Singleton


class SchedulerManager(object, metaclass=Singleton):

    def __init__(self):
        print("Initialisation of the scheduler manager")

        self.scheduler = BackgroundScheduler()
        # create the async loop in the main thread
        self.loop = asyncio.new_event_loop()
        asyncio.set_event_loop(self.loop)  # bind event loop to current thread
        asyncio.get_child_watcher().attach_loop(self.loop)

    def start(self):
        print("Starting scheduler manager")
        if settings.DEBUG:
            # Hook into the apscheduler logger
            logging.basicConfig()
            logging.getLogger('apscheduler').setLevel(logging.DEBUG)
        self.scheduler.start()

        self.add_job_for_each_alarm_clock()

    def play_web_radio(self, url, auto_stop_minutes):
        from restapi.models.backup_file import BackupFile
        backup_files = BackupFile.objects.all()
        backup_file_path = None
        if backup_files is not None:
            backup_file_path = backup_files[0].backup_file.url
            print("Path to the backup MP3: {}".format(backup_file_path))
        print("play_web_radio triggered by scheduler")
        PlayerManager().async_start(self.loop, url, auto_stop_minutes, backup_file_path)
        print("play_web_radio thread terminated")

    def add_job_for_each_alarm_clock(self):
        """
        load all enabled alarm clock from the DB and create a new app scheduler job
        """
        from restapi.models import AlarmClock
        all_alarm_clock = AlarmClock.objects.all()

        for alarm in all_alarm_clock:
            if alarm.enabled:
                self.add_new_job(job_id=alarm.id,
                                 day_of_week_string=alarm.get_day_of_week(),
                                 hour=alarm.hour,
                                 minute=alarm.minute,
                                 url=alarm.webradio.url,
                                 auto_stop_minutes=alarm.auto_stop_minutes)

    def add_new_job(self, job_id, day_of_week_string, hour, minute, url, auto_stop_minutes) -> bool:
        print("add a new job with id {}, {}, {}, {}, {}, {}".
              format(job_id, day_of_week_string, hour, minute, url, auto_stop_minutes))
        my_cron = CronTrigger(hour=hour,
                              minute=minute,
                              day_of_week=day_of_week_string)
        self.scheduler.add_job(func=self.play_web_radio,
                               trigger=my_cron,
                               id=str(job_id),
                               args=[url, auto_stop_minutes])
        return True

    def delete_job_by_id(self, job_id):
        print("removing job id {} form the scheduler".format(job_id))
        try:
            self.scheduler.remove_job(str(job_id))
        except JobLookupError:
            print("Job id {} was already deleted".format(job_id))
