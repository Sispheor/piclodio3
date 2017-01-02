from django.http import Http404
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from webapi.CrontabManager import CrontabManager
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
            # create a job line
            last_alarmclock = AlarmClock.objects.latest('id')
            self.add_job_in_crontab(last_alarmclock)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def add_job_in_crontab(self, alarm):
        """
        use the crontab manager to add a new job
        :param alarm: AlarmClock
        :return:
        """
        day_of_week = self._get_day_of_week(alarm)
        new_job = "%s %s * * %s echo test # piclodio%s" % (alarm.minute, alarm.hour, day_of_week, alarm.id)
        if not alarm.is_active:
            line = "# "
            new_job = line + new_job
        print new_job
        CrontabManager.add_job(new_job)

    @staticmethod
    def _get_day_of_week(alarm):
        """

        :param alarm: AlarmClock
        :type alarm: AlarmClock
        :return:
        """
        def add_el(current_string, el):
            if current_string is not None:
                el = ",%s" % el
                current_string += el
            else:
                current_string = el
            return current_string

        returned_period = None
        if alarm.monday:
            returned_period = add_el(returned_period, "0")
        if alarm.tuesday:
            returned_period = add_el(returned_period, "1")
        if alarm.wednesday:
            returned_period = add_el(returned_period, "2")
        if alarm.thursday:
            returned_period = add_el(returned_period, "3")
        if alarm.friday:
            returned_period = add_el(returned_period, "4")
        if alarm.saturday:
            returned_period = add_el(returned_period, "5")
        if alarm.sunday:
            returned_period = add_el(returned_period, "6")

        return returned_period


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
