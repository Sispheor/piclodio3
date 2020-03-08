from rest_framework.test import APITestCase

from restapi.models import AlarmClock, WebRadio


class TestAlarmClock(APITestCase):

    def setUp(self) -> None:
        super(TestAlarmClock, self).setUp()
        self.webradio = WebRadio.objects.create(name="test", url="http://test.com")

    def test_get_day_of_week(self):
        alarm1 = AlarmClock.objects.create(name="alarm1",
                                                monday=True,
                                                hour=8,
                                                minute=20,
                                                webradio=self.webradio)

        expected = "0"
        self.assertEqual(expected, alarm1.get_day_of_week())

        alarm2 = AlarmClock.objects.create(name="alarm2",
                                           monday=True,
                                           wednesday=True,
                                           hour=8,
                                           minute=20,
                                           webradio=self.webradio)
        expected = "0,2"
        self.assertEqual(expected, alarm2.get_day_of_week())

        alarm3 = AlarmClock.objects.create(name="alarm2",
                                           monday=True,
                                           wednesday=True,
                                           sunday=True,
                                           hour=8,
                                           minute=20,
                                           webradio=self.webradio)
        expected = "0,2,6"
        self.assertEqual(expected, alarm3.get_day_of_week())

