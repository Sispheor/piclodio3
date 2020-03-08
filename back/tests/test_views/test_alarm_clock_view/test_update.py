from rest_framework import status
from rest_framework.reverse import reverse
from unittest.mock import patch
from tests.test_views.test_alarm_clock_view.base import Base
from utils.scheduler_manager import SchedulerManager


class TestUpdate(Base):

    def setUp(self):
        super(TestUpdate, self).setUp()
        self.url = reverse('api:alarmclocks:retrieve_update_destroy',
                           kwargs={'pk': self.test_alarm.id})

        self.update_data = {
            "name": "alarm1_updated",
            "monday": True,
            "is_default": True,
            "hour": 8,
            "minute": 20,
            "enabled": False,
            "webradio": self.test_webradio.id
        }

    def test_update_when_disabled_before_disabled_after(self):

        with patch.object(SchedulerManager, 'delete_job_by_id', return_value=None) as mock_delete_job_by_id:
            with patch.object(SchedulerManager, 'add_new_job', return_value=None) as mock_add_new_job:
                response = self.client.put(self.url, data=self.update_data, format='json')
                self.assertEqual(response.status_code, status.HTTP_200_OK)
                mock_delete_job_by_id.asert_not_called()
                mock_add_new_job.assert_not_called()

    def test_update_when_enabled_before_disabled_after(self):
        self.test_alarm.enabled = True
        self.test_alarm.save()
        with patch.object(SchedulerManager, 'delete_job_by_id', return_value=None) as mock_delete_job_by_id:
            with patch.object(SchedulerManager, 'add_new_job', return_value=None) as mock_add_new_job:
                response = self.client.put(self.url, data=self.update_data, format='json')
                self.assertEqual(response.status_code, status.HTTP_200_OK)
                mock_delete_job_by_id.asert_called_with(self.test_alarm.id)
                mock_add_new_job.assert_not_called()

    def test_update_when_disabled_before_enabled_after(self):
        self.update_data = {
            "name": "alarm1_updated",
            "monday": True,
            "is_default": True,
            "hour": 8,
            "minute": 20,
            "enabled": True,
            "webradio": self.test_webradio.id
        }
        with patch.object(SchedulerManager, 'delete_job_by_id', return_value=None) as mock_delete_job_by_id:
            with patch.object(SchedulerManager, 'add_new_job', return_value=None) as mock_add_new_job:
                response = self.client.put(self.url, data=self.update_data, format='json')
                self.assertEqual(response.status_code, status.HTTP_200_OK)
                mock_delete_job_by_id.asert_called_with(self.test_alarm.id)
                mock_add_new_job.assert_called()
