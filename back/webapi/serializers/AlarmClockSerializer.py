from rest_framework import serializers

from webapi.models import AlarmClock, WebRadio


class AlarmClockSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=250)
    monday = serializers.BooleanField(default=False)
    tuesday = serializers.BooleanField(default=False)
    wednesday = serializers.BooleanField(default=False)
    thursday = serializers.BooleanField(default=False)
    friday = serializers.BooleanField(default=False)
    saturday = serializers.BooleanField(default=False)
    sunday = serializers.BooleanField(default=False)
    hour = serializers.IntegerField(min_value=0, max_value=23)
    minute = serializers.IntegerField(min_value=0, max_value=59)
    is_active = serializers.BooleanField(default=False)
    auto_stop_minutes = serializers.IntegerField(min_value=0, max_value=200, default=0)
    webradio = serializers.PrimaryKeyRelatedField(queryset=WebRadio.objects.all())

    class Meta:
        model = AlarmClock
        fields = ('id', 'name', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'hour',
                  'minute', 'auto_stop_minutes', 'is_active', 'webradio')
