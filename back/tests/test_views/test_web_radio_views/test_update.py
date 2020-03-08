from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from restapi.models import AlarmClock
from restapi.models.web_radio import WebRadio
from utils.scheduler_manager import SchedulerManager
from unittest.mock import patch


class TestUpdate(APITestCase):

    def setUp(self):
        super(TestUpdate, self).setUp()
        self.webradio_to_update = WebRadio.objects.create(name="test", url="http://test.com")
        self.url = reverse('api:webradios:retrieve_update_destroy',
                           kwargs={'pk': self.webradio_to_update.id})

        self.update_data = {
            "name": "updated",
            "url": "http://updated.com",
            "is_default": False
        }

    def test_update(self):

        response = self.client.put(self.url, data=self.update_data, format='json')

        db_updated_webradio = WebRadio.objects.get(id=self.webradio_to_update.id)
        webradio_details = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(webradio_details['id'], db_updated_webradio.id)
        self.assertEqual(webradio_details['name'], db_updated_webradio.name)
        self.assertEqual(webradio_details['url'], db_updated_webradio.url)
        self.assertEqual(webradio_details['is_default'], db_updated_webradio.is_default)

    def test_update_when_linked_to_alarm(self):
        # add an alarm linked to the web radio
        alarm1 = AlarmClock.objects.create(name="alarm1",
                                           monday=True,
                                           hour=8,
                                           minute=20,
                                           webradio=self.webradio_to_update)

        with patch.object(SchedulerManager, 'delete_job_by_id', return_value=None) as mock_delete_job_by_id:
            with patch.object(SchedulerManager, 'add_new_job', return_value=None) as mock_add_new_job:
                self.client.put(self.url, data=self.update_data, format='json')
                mock_delete_job_by_id.assert_called_with(alarm1.id)
                mock_add_new_job.assert_called_with(job_id=alarm1.id,
                                                    day_of_week_string=alarm1.get_day_of_week(),
                                                    hour=alarm1.hour,
                                                    minute=alarm1.minute,
                                                    url="http://updated.com",
                                                    auto_stop_minutes=alarm1.auto_stop_minutes)
