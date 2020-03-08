from rest_framework import status
from rest_framework.reverse import reverse
from unittest.mock import patch
from restapi.models import AlarmClock
from tests.test_views.test_alarm_clock_view.base import Base
from utils.scheduler_manager import SchedulerManager


class TestDelete(Base):

    def setUp(self):
        super(TestDelete, self).setUp()
        self.url = reverse('api:alarmclocks:retrieve_update_destroy',
                           kwargs={'pk': self.test_alarm.id})

    def test_delete(self):
        with patch.object(SchedulerManager, 'delete_job_by_id', return_value=None) as mock_scheduler:
            response = self.client.delete(self.url, format='json')
            self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
            self.assertEqual(AlarmClock.objects.count(), 1)
            mock_scheduler.assert_called_with(self.test_alarm.id)
        # the alarm clock should be deleted
        with self.assertRaises(AlarmClock.DoesNotExist):
            AlarmClock.objects.get(pk=self.test_alarm.id)
