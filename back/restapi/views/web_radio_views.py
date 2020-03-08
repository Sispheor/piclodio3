from rest_framework import generics

from restapi.models import AlarmClock
from restapi.models .web_radio import WebRadio
from restapi.serializers.web_radio_serializer import WebRadioSerializer


class WebRadioList(generics.ListCreateAPIView):
    queryset = WebRadio.objects.all()
    serializer_class = WebRadioSerializer


class WebRadioDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = WebRadio.objects.all()
    serializer_class = WebRadioSerializer

    def perform_update(self, serializer):
        """
        When updating a webradio, if this one is linked to an enabled alarm,
        we need to recreate the job into the scheduler with the new URL
        """
        instance = serializer.save()
        from utils.scheduler_manager import SchedulerManager
        scheduler_manager = SchedulerManager()
        # find all enabled alarm that are currently using this web radio
        alarms = AlarmClock.objects.filter(webradio=instance)
        for alarm in alarms:
            # delete first all concerned alarms
            scheduler_manager.delete_job_by_id(alarm.id)
            if alarm.enabled:
                # then create back to update
                scheduler_manager.add_new_job(job_id=alarm.id,
                                              day_of_week_string=alarm.get_day_of_week(),
                                              hour=alarm.hour,
                                              minute=alarm.minute,
                                              url=alarm.webradio.url,
                                              auto_stop_minutes=alarm.auto_stop_minutes)
