from time import sleep

from django.test import TestCase

# from webapi.CrontabManager import CrontabManager
#
# # test get
# contab = CrontabManager.get_current_crontab()


# # test add new job
# new_newcron = "0 7 * * * echo test # piclodio 3"
# CrontabManager.add_job(job=new_newcron)
#
# CrontabManager.get_current_crontab()

# test disable
# test = "piclodio 1"
# print CrontabManager.disable_job(test)

# test enable
# test = "piclodio 1"
# CrontabManager.enable_job(test)

# test remove
# test = "piclodio 2"
# CrontabManager.remove_job(test)
from webapi.PlayerManager import PlayerManager
# from webapi.models import AlarmClock, BackupMusic

# all_jobs = BackupMusic.objects.all()
#
# for el in all_jobs:
#     el.delete()

# url = "http://192.99.17.12:6410/"
#
# PlayerManager.stop()

import threading


class ThreadTimeout(object):
    def __init__(self, callback_instance, backup_instance, timeout):
        self.callback_instance = callback_instance
        self.backup_instance = backup_instance
        self.timeout = timeout
        self.main_thread = None

    def run(self):
        def target():
            print 'Thread started'
            self.callback_instance.start()
            print 'Thread finished'

        def waiting_target():
            print "Wait %s seconds before checking is the thread is alive" % self.timeout
            sleep(self.timeout)
            if self.main_thread.is_alive():
                print 'Thread is alive'
                # thread.join()
            else:
                print 'Thread is dead'
                if self.backup_instance is not None:
                    print "Playing backup file"
                    self.backup_instance.start()
                else:
                    print "Not backup file provided"

        # start a thread to play the webradio
        self.main_thread = threading.Thread(target=target)
        self.main_thread.start()

        # start a thread that will check that the first thread is alive
        thread_waiting = threading.Thread(target=waiting_target)
        thread_waiting.start()



class CallbackPlayer(object):
    def __init__(self, url=None):
        self.url = url

    def start(self):
        PlayerManager.play(self.url)


# working url
url = "http://192.99.17.12:6410/"

# not working url
#url = "http://192.99.17.10:6410/"
backup_mp3 = "/home/nico/Desktop/mpthreetest.mp3"

url_player = CallbackPlayer(url=url)
backup_mp3player = CallbackPlayer(url=backup_mp3)


command = ThreadTimeout(callback_instance=url_player, backup_instance=backup_mp3player, timeout=45)
command.run()


# print "wait 5 sec"
# sleep(5)
# print "kill player"
# PlayerManager.stop()

