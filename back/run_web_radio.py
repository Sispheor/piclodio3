import os
import sys
import django
from webapi.PlayerManager import CallbackPlayer, ThreadTimeout

# load django models
project_path = os.path.dirname(os.path.realpath(__file__))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "piclodio3.settings")
sys.path.append(project_path)
django.setup()
from webapi.models import WebRadio, BackupMusic

# get the ID of the webradio to play from the argument
id_web_radio_to_play = sys.argv[1]
print "Id of the web radio to play: %s" % id_web_radio_to_play
# get the time in minute before auto kill
minute_before_auto_kill = None
try:
    minute_before_auto_kill = sys.argv[2]
    print "Auto kill the web radio in %s minutes" % minute_before_auto_kill
except IndexError:
    print "No minutes for auto kill"

# get the real web radio object to play
try:
    web_radio_to_play = WebRadio.objects.get(id=id_web_radio_to_play)
except WebRadio.DoesNotExist:
    print "The web radio id %s does not exist, cannot launch"
    sys.exit()

# try to get a backup mp3
backup_mp3_list = BackupMusic.objects.all()
backup_mp3_path = None
if backup_mp3_list is not None:
    if len(backup_mp3_list) == 1:
        backup_mp3_path = backup_mp3_list[0].backup_file.url
        print "Path to the backup MP3: %s" % backup_mp3_path

# start the thread that will play the web radio, check that the web radio is playing, and auto kill it if needed
web_radio_callback = CallbackPlayer(url=web_radio_to_play.url)
backup_mp3_callback = None
if backup_mp3_path is not None:
    backup_mp3_callback = CallbackPlayer(url=backup_mp3_path)

command = ThreadTimeout(callback_instance=web_radio_callback,
                        backup_instance=backup_mp3_callback,
                        timeout=5,
                        time_before_auto_kill=minute_before_auto_kill)
command.run()




