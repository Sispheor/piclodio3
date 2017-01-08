from __future__ import unicode_literals

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
    auto_stop_minutes = models.IntegerField(default=0)
    webradio = models.ForeignKey(WebRadio)


class BackupMusic(models.Model):
    backup_file = models.FileField(upload_to="backup_mp3")
