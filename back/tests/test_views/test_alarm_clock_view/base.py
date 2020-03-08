from rest_framework.test import APITestCase

from restapi.models import WebRadio, AlarmClock


class Base(APITestCase):
    def setUp(self):
        super(Base, self).setUp()

        self.test_webradio = WebRadio.objects.create(name="test", url="http://test.com")
        self.test_webradio2 = WebRadio.objects.create(name="test2", url="http://test2.com")
        self.test_alarm = AlarmClock.objects.create(name="alarm1",
                                                    monday=True,
                                                    hour=8,
                                                    minute=20,
                                                    webradio=self.test_webradio)
        self.test_alarm2 = AlarmClock.objects.create(name="alarm2",
                                                     wednesday=True,
                                                     hour=8,
                                                     minute=20,
                                                     webradio=self.test_webradio2)
