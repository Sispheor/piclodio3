import sys

from django.apps import AppConfig

from utils.scheduler_manager import SchedulerManager


class RestapiConfig(AppConfig):
    name = 'restapi'

    def __init__(self, app_name, app_module):
        super().__init__(app_name, app_module)

    def ready(self):
        argv = sys.argv
        list_banned_argument = ["makemigrations", "migrate", "collectstatic", "dumpdata", "loaddata"]
        if [i for i in list_banned_argument if i not in argv]:
            # start the scheduler
            scheduler_manager = SchedulerManager()
            scheduler_manager.start()

            # active signals
            import restapi.signals
