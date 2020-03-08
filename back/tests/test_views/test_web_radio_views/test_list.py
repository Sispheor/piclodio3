from collections import OrderedDict

from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from restapi.models.web_radio import WebRadio


class TestList(APITestCase):

    def setUp(self):
        super(TestList, self).setUp()
        self.url = reverse('api:webradios:list_create')

        self.webradio1 = WebRadio.objects.create(name="test", url="http://test.com")
        self.webradio2 = WebRadio.objects.create(name="test2", url="http://test2.com", is_default=True)

    def test_list(self):
        response = self.client.get(self.url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        expected = OrderedDict([('count', 2),
                                ('next', None),
                                ('previous', None),
                                ('results', [OrderedDict([('id', self.webradio1.id),
                                                          ('name', 'test'),
                                                          ('url', 'http://test.com'),
                                                          ('is_default', False)]),
                                             OrderedDict([('id', self.webradio2.id),
                                                          ('name', 'test2'),
                                                          ('url', 'http://test2.com'),
                                                          ('is_default', True)])])])
        self.assertEqual(expected, response.data)
