from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from restapi.models.web_radio import WebRadio


class TestCreate(APITestCase):

    def setUp(self):
        super(TestCreate, self).setUp()
        self.url = reverse('api:webradios:list_create')

    def test_can_create(self):
        data = {
            "name": "test",
            "url": "http://test.com",
            "is_default": True
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(WebRadio.objects.count(), 1)
        self.assertEqual(WebRadio.objects.get().name, 'test')
