from __future__ import unicode_literals

from django.db import models


class WebRadio(models.Model):
    name = models.CharField(max_length=250)
    url = models.CharField(max_length=250)
    # a default WebRadio is the web radio the user can launch when click on play.
    # The last started web radio become the default one
    is_default = models.BooleanField(default=False)


class DayOfWeek(models.Model):
    monday = models.BooleanField(default=False)
    tuesday = models.BooleanField(default=False)
    wednesday = models.BooleanField(default=False)
    thursday = models.BooleanField(default=False)
    friday = models.BooleanField(default=False)
    saturday = models.BooleanField(default=False)
    sunday = models.BooleanField(default=False)


class AlarmClock(models.Model):
    name = models.CharField(max_length=250)
    dayofweek = models.ForeignKey(DayOfWeek, on_delete=models.CASCADE)
    hour = models.IntegerField()
    minute = models.IntegerField()
    is_active = models.BooleanField(default=False)
    webradio = models.ForeignKey(WebRadio)
