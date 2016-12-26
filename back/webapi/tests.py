from django.test import TestCase

# Create your tests here.
from webapi.models import WebRadio, DayOfWeek, AlarmClock

webradio = WebRadio.objects.get(id=2)

dayofweek = DayOfWeek()
dayofweek.monday = True
dayofweek.save()

alarm1 = AlarmClock()
alarm1.hour = 7
alarm1.minute = 30
alarm1.dayofweek = dayofweek
alarm1.webradio = webradio

alarm1.save()