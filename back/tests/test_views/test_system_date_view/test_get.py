from datetime import datetime
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase


class TestGet(APITestCase):

    def setUp(self):
        super(TestGet, self).setUp()
        self.url = reverse('api:clock:get_clock')

    def test_get_details(self):
        response = self.client.get(self.url, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue("clock" in response.data)
        self.assertTrue(self.validate_date(response.data["clock"]))

    @staticmethod
    def validate_date(date_text):
        try:
            datetime.strptime(date_text, '%Y-%m-%dT%H:%M:%S')
            return True
        except ValueError:
            pass
        return False
