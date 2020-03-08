from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from restapi.models import AlarmClock
from restapi.models.web_radio import WebRadio


class TestDelete(APITestCase):

    def setUp(self):
        super(TestDelete, self).setUp()
        self.webradio_to_delete = WebRadio.objects.create(name="test", url="http://test.com")
        self.url = reverse('api:webradios:retrieve_update_destroy',
                           kwargs={'pk': self.webradio_to_delete.id})

    def test_delete(self):
        response = self.client.delete(self.url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(WebRadio.objects.count(), 0)

    def test_delete_with_alarm_clock(self):
        should_be_deleted_alarm_clock = AlarmClock.objects.create(name="alarm1",
                                                                  monday=True,
                                                                  hour=8,
                                                                  minute=20,
                                                                  webradio=self.webradio_to_delete)

        from utils.scheduler_manager import SchedulerManager
        from unittest.mock import patch
        with patch.object(SchedulerManager, 'delete_job_by_id', return_value=None) as mock_scheduler:
            self.client.delete(self.url, format='json')
            mock_scheduler.assert_called_with(should_be_deleted_alarm_clock.id)
        # the linked alarm clock should be deleted
        with self.assertRaises(AlarmClock.DoesNotExist):
            AlarmClock.objects.get(pk=should_be_deleted_alarm_clock.id)
