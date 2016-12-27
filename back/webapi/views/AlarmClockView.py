from django.http import Http404
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from webapi.models import AlarmClock
from webapi.serializers.AlarmClockSerializer import AlarmClockSerializer


class AlarmClockList(APIView):
    permission_classes = (AllowAny,)
    serializer_class = AlarmClockSerializer

    def get(self, request, format=None):
        alarmclocks = AlarmClock.objects.all()
        serializer = AlarmClockSerializer(alarmclocks, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = AlarmClockSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AlarmClockDetail(APIView):
    """
    Retrieve, update or delete a WebRadio instance.
    """
    permission_classes = (AllowAny,)
    serializer_class = AlarmClockSerializer

    def get_object(self, pk):
        try:
            return AlarmClock.objects.get(pk=pk)
        except AlarmClock.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        alarmclock = self.get_object(pk)
        serializer = AlarmClockSerializer(alarmclock)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        alarmclock = self.get_object(pk)
        serializer = AlarmClockSerializer(alarmclock, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        alarmclock = self.get_object(pk)
        alarmclock.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
