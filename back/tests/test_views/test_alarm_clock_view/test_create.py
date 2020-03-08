from rest_framework import status
from rest_framework.reverse import reverse
from unittest.mock import patch
from restapi.models import AlarmClock
from tests.test_views.test_alarm_clock_view.base import Base
from utils.scheduler_manager import SchedulerManager


class TestCreate(Base):

    def setUp(self):
        super(TestCreate, self).setUp()
        self.url = reverse('api:alarmclocks:list_create')

    def test_create(self):

        data = {
            "name": "test3",
            "monday": True,
            "is_default": True,
            "hour": 8,
            "minute": 20,
            "enabled": False,
            "webradio": self.test_webradio.id
        }

        with patch.object(SchedulerManager, 'add_new_job', return_value=None) as mock_scheduler:
            response = self.client.post(self.url, data, format='json')
            self.assertEqual(response.status_code, status.HTTP_201_CREATED)
            self.assertEqual(AlarmClock.objects.count(), 3)
            mock_scheduler.assert_not_called()

    def test_create_when_enabled(self):
        data = {
            "name": "test3",
            "monday": True,
            "is_default": True,
            "hour": 8,
            "minute": 20,
            "enabled": True,
            "webradio": self.test_webradio.id
        }

        with patch.object(SchedulerManager, 'add_new_job', return_value=None) as mock_scheduler:
            response = self.client.post(self.url, data, format='json')
            self.assertEqual(response.status_code, status.HTTP_201_CREATED)
            self.assertEqual(AlarmClock.objects.count(), 3)
            mock_scheduler.assert_called()
