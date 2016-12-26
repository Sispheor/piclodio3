from rest_framework import serializers

from webapi.models import DayOfWeek, AlarmClock, WebRadio
from webapi.serializers.DayOfWeekSerializer import DayOfWeekSerializer
from webapi.serializers.WebRadioSerializer import WebRadioSerializer


class AlarmClockReadOnlySerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=250)
    dayofweek = DayOfWeekSerializer(read_only=True)
    hour = serializers.IntegerField(min_value=0, max_value=23)
    minute = serializers.IntegerField(min_value=0, max_value=59)
    is_active = serializers.BooleanField(default=False)
    webradio = WebRadioSerializer(read_only=True)

    class Meta:
        model = AlarmClock
        fields = ('id', 'name', 'dayofweek', 'hour', 'minute', 'is_active', 'webradio')


class AlarmClockSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=250)
    dayofweek = DayOfWeekSerializer()
    hour = serializers.IntegerField(min_value=0, max_value=23)
    minute = serializers.IntegerField(min_value=0, max_value=59)
    is_active = serializers.BooleanField(default=False)
    webradio = serializers.PrimaryKeyRelatedField(queryset=WebRadio.objects.all())

    class Meta:
        model = AlarmClock
        fields = ('id', 'name', 'dayofweek', 'hour', 'minute', 'is_active', 'webradio')
