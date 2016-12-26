from django.http import Http404
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from webapi.models import AlarmClock, DayOfWeek, WebRadio
from webapi.serializers.AlarmClockSerializer import AlarmClockSerializer, AlarmClockReadOnlySerializer


class AlarmClockList(APIView):
    permission_classes = (AllowAny,)
    serializer_class = AlarmClockSerializer

    def get(self, request, format=None):
        alarmclocks = AlarmClock.objects.all()
        serializer = AlarmClockReadOnlySerializer(alarmclocks, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = AlarmClockSerializer(data=request.data)
        if serializer.is_valid():
            # create a dict with data sent
            dict_of_value = serializer.data
            # print dict_of_value
            # create the dayofweek object first
            new_dayofweek = DayOfWeek(**dict_of_value["dayofweek"])
            new_dayofweek.save()
            # we remove the info about the day of week from the dict
            del dict_of_value["dayofweek"]
            # get the target webradio from the sent id
            webradio = WebRadio.objects.get(id=dict_of_value["webradio"])
            # same here, we delete the webradio info as it's not an object
            del dict_of_value["webradio"]
            # create alarm with the dict of valid parameters
            new_alarm = AlarmClock(**dict_of_value)
            new_alarm.dayofweek = new_dayofweek
            new_alarm.webradio = webradio
            new_alarm.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
