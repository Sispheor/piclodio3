from unittest.mock import patch

from rest_framework import status
from rest_framework.exceptions import ErrorDetail
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from utils.sound_manager import SoundManager


class TestUpdate(APITestCase):

    def setUp(self):
        super(TestUpdate, self).setUp()
        self.url = reverse('api:volume:get_or_update_volume')

    def test_set_volume_invalid(self):
        data = {
            "volume": 200
        }
        response = self.client.post(self.url, data, format='json')
        expected = {'volume':
                        [ErrorDetail(string='Ensure this value is less than or equal to 100.',
                                     code='max_value')]}
        self.assertEquals(expected, response.data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_set_volume(self):
        data = {
            "volume": 100
        }
        with patch.object(SoundManager, 'set_volume', return_value=10) as mock_sound_manager:
            response = self.client.post(self.url, data, format='json')
            expected = {'volume': 100}
            self.assertEquals(expected, response.data)
            mock_sound_manager.assert_called()
