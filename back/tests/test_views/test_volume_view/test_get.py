from unittest.mock import patch
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from utils.sound_manager import SoundManager


class TestGet(APITestCase):

    def setUp(self):
        super(TestGet, self).setUp()
        self.url = reverse('api:volume:get_or_update_volume')

    def test_get_volume(self):

        with patch.object(SoundManager, 'get_volume', return_value=10) as mock_sound_manager:
            response = self.client.get(self.url, format='json')
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.assertTrue("volume" in response.data)
            self.assertEquals(10, response.data["volume"])
            mock_sound_manager.assert_called()

