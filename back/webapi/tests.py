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


class Command(object):
    def __init__(self, callback_function):
        self.callback_function = callback_function

    def run(self, timeout):
        def target():
            print 'Thread started'
            self.callback_function()
            print 'Thread finished'

        thread = threading.Thread(target=target)
        thread.start()
        print "Wait %s seconds before checking is the thread is alive" % timeout
        thread.join(timeout)
        if thread.is_alive():
            print 'Thread is alive'
            # thread.join()


def callback():
    url = "http://192.99.17.12:6410/"
    PlayerManager.play(url)

command = Command(callback_function=callback)
command.run(timeout=3)


print "wait 5 sec"
sleep(5)
print "kill player"
PlayerManager.stop()

