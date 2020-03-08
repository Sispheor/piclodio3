import os
import time
from unittest.mock import patch
import tempfile

from django.conf import settings
from rest_framework import status
from rest_framework.exceptions import ErrorDetail
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase


class TestCreate(APITestCase):

    def setUp(self):
        super(TestCreate, self).setUp()
        self.url = reverse('api:backup:list_create')

        self.valid_file = "/tmp/test_upload.mp3"
        self.invalid_file = "/tmp/test_upload.not_supported"

        # settings.MEDIA_ROOT = tempfile.mkdtemp()

    def tearDown(self) -> None:
        if os.path.exists(self.valid_file):
            os.remove(self.valid_file)

    @staticmethod
    def _create_test_file(path):
        f = open(path, 'w')
        f.write('test123\n')
        f.close()
        f = open(path, 'rb')
        return {'backup_file': f}

    def test_upload_valid_backup_file(self):
        data = self._create_test_file(self.valid_file)

        response = self.client.post(self.url, data, format='multipart')
        expected = {'id': 1, 'backup_file': 'backup_mp3/test_upload.mp3'}
        self.assertEquals(expected, response.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_upload_invalid_backup_file(self):
        data = self._create_test_file(self.invalid_file)
        response = self.client.post(self.url, data, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
