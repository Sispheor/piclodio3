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
from webapi.PlayerManager import PlayerManager, CallbackPlayer, ThreadTimeout

# from webapi.models import AlarmClock, BackupMusic

# all_jobs = BackupMusic.objects.all()
#
# for el in all_jobs:
#     el.delete()

# url = "http://192.99.17.12:6410/"
#
# PlayerManager.stop()




# working url
url = "http://192.99.17.12:6410/"

# not working url
url = "http://192.99.17.10:6410/"
backup_mp3 = "/home/nico/Desktop/mpthreetest.mp3"

url_player = CallbackPlayer(url=url)
backup_mp3player = CallbackPlayer(url=backup_mp3)


command = ThreadTimeout(callback_instance=url_player, backup_instance=backup_mp3player, timeout=45)
command.run()


# print "wait 5 sec"
# sleep(5)
# print "kill player"
# PlayerManager.stop()

