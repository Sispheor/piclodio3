from rest_framework import status
from rest_framework.exceptions import ErrorDetail
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase
from unittest.mock import patch
from restapi.models.web_radio import WebRadio
from utils.player_manager import PlayerManager


class TestUpdate(APITestCase):

    def setUp(self):
        super(TestUpdate, self).setUp()
        self.url = reverse('api:player:get_player_or_update')

    def test_update_wrong_data_sent(self):
        data = {
            "active": "wrong",
            "webradio": 12,
        }
        response = self.client.post(self.url, data, format='json')
        expected = {'active': [ErrorDetail(string='Must be a valid boolean.', code='invalid')],
                    'webradio': [ErrorDetail(string='Invalid pk "12" - object does not exist.', code='does_not_exist')]}
        self.assertEquals(expected, response.data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_update_web_radio_do_not_exist(self):
        data = {
            "active": True,
            "webradio": 12,
        }
        response = self.client.post(self.url, data, format='json')
        expected = {'webradio': [ErrorDetail(string='Invalid pk "12" - object does not exist.', code='does_not_exist')]}
        self.assertEquals(expected, response.data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_update_with_default_webradio_no_webradio_provided(self):
        WebRadio.objects.create(name="test", url="http://test.com", is_default=True)
        data = {
            "active": True
        }

        with patch.object(PlayerManager, 'threaded_start', return_value=True) as mock_player_start:
            response = self.client.post(self.url, data, format='json')
            expected = {'active': True,
                        'webradio': {'id': 1, 'name': 'test', 'url': 'http://test.com', 'is_default': True}}
            self.assertEquals(expected, response.data)
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            mock_player_start.assert_called()

    def test_update_with_default_webradio_and_webradio_provided(self):
        WebRadio.objects.create(name="test", url="http://test.com", is_default=True)
        WebRadio.objects.create(name="test2", url="http://test2.com")

        data = {
            "active": True,
            "webradio": 2
        }

        with patch.object(PlayerManager, 'threaded_start', return_value=True) as mock_player_start:
            response = self.client.post(self.url, data, format='json')
            expected = {'active': True,
                        'webradio': {'id': 2, 'name': 'test2', 'url': 'http://test2.com', 'is_default': True}}
            self.assertEquals(expected, response.data)
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            # check that the default web radio is now the one we asked
            web_radio1 = WebRadio.objects.get(pk=1)
            web_radio2 = WebRadio.objects.get(pk=2)
            self.assertFalse(web_radio1.is_default)
            self.assertTrue(web_radio2.is_default)
            mock_player_start.assert_called()

    def test_update_no_default_webradio_no_webradio_provided(self):

        data = {
            "active": True
        }
        response = self.client.post(self.url, data, format='json')
        expected = {'status': 'error, no default web radio. Please specify one'}
        self.assertEquals(expected, response.data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_stop_player(self):
        data = {
            "active": False
        }
        with patch.object(PlayerManager, 'stop', return_value=True) as mock_stop_player:
            response = self.client.post(self.url, data, format='json')
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            mock_stop_player.assert_called()
