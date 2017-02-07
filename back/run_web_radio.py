"""
This script is used to start a web radio from its database ID passed as argument.
The script can also handle the automatic stop with a second argument.

How to use: python run_web_radio.py <id_web_radio> [<minutes_before_auto_stop>]
E.g: python run_web_radio.py 12 20
"""
import os
import sys
import urllib2
import django
from webapi.Utils.PlayerManager import CallbackPlayer, ThreadTimeout


def is_url_valid(url):
    """
    Test if we can get a TCP connection to the target URL
    :param url: url to check
    :return: True if the metode can connect to the URL
    """
    try:
        print("Try to connect to the URL: %s" % url)
        connection = urllib2.urlopen(url, timeout=5)
        print("URL status code: %s " % connection.getcode())
        connection.close()
        return True
    except urllib2.HTTPError:
        print("Failed to connect")
        return False
    except urllib2.URLError:
        print("Failed to connect (timeout)")
        return False


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

# try to get a backup mp3 if exists
backup_mp3_list = BackupMusic.objects.all()
backup_mp3_path = None
backup_mp3_callback = None
if backup_mp3_list is not None:
    if len(backup_mp3_list) == 1:
        backup_mp3_path = backup_mp3_list[0].backup_file.url
        print "Path to the backup MP3: %s" % backup_mp3_path
        if backup_mp3_path is not None:
            backup_mp3_callback = CallbackPlayer(url=backup_mp3_path)

# test the URL, if this one is not valid, we start the backup
if is_url_valid(url=web_radio_to_play.url):
    # start the thread that will play the web radio, check that the web radio is playing, and auto kill it if needed
    web_radio_callback = CallbackPlayer(url=web_radio_to_play.url)
    # the following thread will start to play the web radio and then check if the player is still alive after 35 seconds
    # this to prevent the case where the URL is valid and is answering request but no stream is present inside
    command = ThreadTimeout(callback_instance=web_radio_callback,
                            backup_instance=backup_mp3_callback,
                            timeout=35,
                            time_before_auto_kill=minute_before_auto_kill)
    command.run()
else:
    # the URL is not valid, start the backup MP3 if exist
    if backup_mp3_callback is not None:
        backup_mp3_callback.start()



