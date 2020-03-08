from collections import OrderedDict
from rest_framework import status
from rest_framework.reverse import reverse
from tests.test_views.test_alarm_clock_view.base import Base


class TestList(Base):

    def setUp(self):
        super(TestList, self).setUp()
        self.url = reverse('api:alarmclocks:list_create')

    def test_list(self):
        response = self.client.get(self.url, format='json')

        expected = OrderedDict(
            [('count', 2),
             ('next', None),
             ('previous', None),
             ('results', [
                 OrderedDict([('id', 1),
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
                              ('webradio', 1)]),
                 OrderedDict([('id', 2),
                              ('name', 'alarm2'),
                              ('monday', False),
                              ('tuesday', False),
                              ('wednesday', True),
                              ('thursday', False),
                              ('friday', False),
                              ('saturday', False),
                              ('sunday', False),
                              ('hour', 8),
                              ('minute', 20),
                              ('enabled', True),
                              ('auto_stop_minutes', 0),
                              ('webradio', 2)])])])
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(expected, response.data)
