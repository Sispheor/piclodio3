from rest_framework import generics, status
from rest_framework.response import Response

from restapi.models import AlarmClock
from restapi.serializers.alarm_clock_serializer import AlarmClockSerializer


class AlarmClockList(generics.ListCreateAPIView):
    queryset = AlarmClock.objects.all()
    serializer_class = AlarmClockSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        saved_alarm = serializer.save()

        if saved_alarm.enabled:
            # get the current instance of the scheduler
            from utils.scheduler_manager import SchedulerManager
            scheduler_manager = SchedulerManager()
            scheduler_manager.add_new_job(job_id=saved_alarm.id,
                                          day_of_week_string=saved_alarm.get_day_of_week(),
                                          hour=saved_alarm.hour,
                                          minute=saved_alarm.minute,
                                          url=saved_alarm.webradio.url,
                                          auto_stop_minutes=saved_alarm.auto_stop_minutes)

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class AlarmClockDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = AlarmClock.objects.all()
    serializer_class = AlarmClockSerializer

    def perform_destroy(self, instance):
        from utils.scheduler_manager import SchedulerManager
        scheduler_manager = SchedulerManager()
        scheduler_manager.delete_job_by_id(instance.id)
        instance.delete()

    def perform_update(self, serializer):
        instance = serializer.save()
        from utils.scheduler_manager import SchedulerManager
        scheduler_manager = SchedulerManager()
        if instance.enabled:
            # delete first
            scheduler_manager.delete_job_by_id(instance.id)
            # then create back to update
            scheduler_manager.add_new_job(job_id=instance.id,
                                          day_of_week_string=instance.get_day_of_week(),
                                          hour=instance.hour,
                                          minute=instance.minute,
                                          url=instance.webradio.url,
                                          auto_stop_minutes=instance.auto_stop_minutes)
        else:
            scheduler_manager.delete_job_by_id(instance.id)
