from __future__ import unicode_literals

import os
import subprocess
from django.db import models


class WebRadio(models.Model):
    name = models.CharField(max_length=250)
    url = models.CharField(max_length=250)
    # a default WebRadio is the web radio the user can launch when click on play.
    # The last started web radio become the default one
    is_default = models.BooleanField(default=False)


class AlarmClock(models.Model):
    name = models.CharField(max_length=250)
    monday = models.BooleanField(default=False)
    tuesday = models.BooleanField(default=False)
    wednesday = models.BooleanField(default=False)
    thursday = models.BooleanField(default=False)
    friday = models.BooleanField(default=False)
    saturday = models.BooleanField(default=False)
    sunday = models.BooleanField(default=False)
    hour = models.IntegerField()
    minute = models.IntegerField()
    is_active = models.BooleanField(default=False)
    webradio = models.ForeignKey(WebRadio)


class BackupMusic(models.Model):
    backup_file = models.FileField(upload_to="backup_mp3")


class Player(object):
    """
    Class to play music with mplayer
    """
    MPLAYER_EXEC_PATH = "/usr/bin/mplayer"

    @classmethod
    def play(cls, url):
        # kill process if already running
        if cls.is_started():
            cls.stop()
        mplayer_exec_path = [cls.MPLAYER_EXEC_PATH]
        mplayer_options = ['-slave', '-quiet']
        mplayer_command = list()
        mplayer_command.extend(mplayer_exec_path)
        mplayer_command.extend(mplayer_options)

        mplayer_command.extend([url])
        print("Mplayer cmd: %s" % str(mplayer_command))

        fnull = open(os.devnull, 'w')

        subprocess.Popen(mplayer_command, stdout=fnull, stderr=fnull)

    @classmethod
    def stop(cls):
        """
        Kill mplayer process
        """
        p = subprocess.Popen("killall mplayer", shell=True)
        p.communicate()

    @classmethod
    def is_started(cls):
        # check number of process
        p = subprocess.Popen("pgrep mplayer", stdout=subprocess.PIPE, shell=True)
        (output, err) = p.communicate()
        if output == "":
            return False
        else:
            return True
