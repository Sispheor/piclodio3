from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase
from unittest.mock import patch

from restapi.models import WebRadio
from utils.player_manager import PlayerManager


class TestGet(APITestCase):

    def setUp(self):
        super(TestGet, self).setUp()
        self.url = reverse('api:player:get_player_or_update')

    def test_get_when_player_stopped_no_web_radio(self):
        response = self.client.get(self.url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue("active" in response.data)
        self.assertFalse(response.data["active"])
        expected = {'active': False, 'webradio': 'no default web radio yet'}
        self.assertEquals(expected, response.data)

    def test_get_when_player_started(self):
        WebRadio.objects.create(name="test", url="http://test.com", is_default=True)
        with patch.object(PlayerManager, 'is_started', return_value=True):
            response = self.client.get(self.url, format='json')
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.assertTrue("active" in response.data)
            self.assertTrue(response.data["active"])
            expected = {'active': True,
                        'webradio': {'id': 1, 'name': 'test', 'url': 'http://test.com', 'is_default': True}}
            self.assertEquals(expected, response.data)
