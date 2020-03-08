from collections import OrderedDict
from rest_framework import status
from rest_framework.reverse import reverse
from tests.test_views.test_alarm_clock_view.base import Base


class TestGetDetails(Base):

    def setUp(self):
        super(TestGetDetails, self).setUp()
        self.url = reverse('api:alarmclocks:retrieve_update_destroy', args=[self.test_webradio.id])

    def test_get_details(self):
        response = self.client.get(self.url, format='json')

        expected_response = OrderedDict([('id', 1),
                                         ('name', 'alarm1'),
                                         ('monday', True),
                                         ('tuesday', False),
                                         ('wednesday', False),
                                         ('thursday', False),
                                         ('friday', False),
                                         ('saturday', False),
                                         ('sunday', False),
                                         ('hour', 8),
                                         ('minute', 20),
                                         ('enabled', True),
                                         ('auto_stop_minutes', 0),
                                         ('webradio', 1)
                                         ]
                                        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(expected_response, response.json())
