from rest_framework import serializers

from webapi.models import DayOfWeek


class DayOfWeekSerializer(serializers.ModelSerializer):
    monday = serializers.BooleanField(default=False)
    tuesday = serializers.BooleanField(default=False)
    wednesday = serializers.BooleanField(default=False)
    thursday = serializers.BooleanField(default=False)
    friday = serializers.BooleanField(default=False)
    saturday = serializers.BooleanField(default=False)
    sunday = serializers.BooleanField(default=False)

    class Meta:
        model = DayOfWeek
        fields = ('monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday')
