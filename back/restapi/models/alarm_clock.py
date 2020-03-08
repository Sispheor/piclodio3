from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from restapi.models.web_radio import WebRadio


class AlarmClock(models.Model):
    name = models.CharField(max_length=250)
    monday = models.BooleanField(default=False)
    tuesday = models.BooleanField(default=False)
    wednesday = models.BooleanField(default=False)
    thursday = models.BooleanField(default=False)
    friday = models.BooleanField(default=False)
    saturday = models.BooleanField(default=False)
    sunday = models.BooleanField(default=False)
    hour = models.IntegerField(validators=[
        MaxValueValidator(23),
        MinValueValidator(0)
    ])
    minute = models.IntegerField(validators=[
        MaxValueValidator(59),
        MinValueValidator(0)
    ])
    enabled = models.BooleanField(default=True)
    auto_stop_minutes = models.IntegerField(default=0)
    webradio = models.ForeignKey(WebRadio, on_delete=models.CASCADE)

    def get_day_of_week(self):
        """
        get a valid day of week period string usable with crontab
        """

        def add_el(current_string, el):
            if current_string is not None:
                el = ",%s" % el
                current_string += el
            else:
                current_string = el
            return current_string

        returned_period = None
        if self.monday:
            returned_period = add_el(returned_period, "0")
        if self.tuesday:
            returned_period = add_el(returned_period, "1")
        if self.wednesday:
            returned_period = add_el(returned_period, "2")
        if self.thursday:
            returned_period = add_el(returned_period, "3")
        if self.friday:
            returned_period = add_el(returned_period, "4")
        if self.saturday:
            returned_period = add_el(returned_period, "5")
        if self.sunday:
            returned_period = add_el(returned_period, "6")

        return returned_period
