from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from restapi.models.web_radio import WebRadio


class TestGetDetails(APITestCase):

    def setUp(self):
        super(TestGetDetails, self).setUp()
        self.webradio = WebRadio.objects.create(name="test", url="http://test.com")
        self.url = reverse('api:webradios:retrieve_update_destroy', args=[self.webradio.id])

    def test_get_details(self):
        response = self.client.get(self.url, format='json')
        expected_response = {'id': self.webradio.id, 'is_default': False, 'name': 'test', 'url': 'http://test.com'}
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(expected_response, response.json())
