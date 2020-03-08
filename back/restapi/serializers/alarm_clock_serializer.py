from rest_framework import serializers

from restapi.models import AlarmClock


class AlarmClockSerializer(serializers.ModelSerializer):

    def validate(self, data):
        """
        Check that start is before finish.
        """
        if not data['monday'] \
                and not data['tuesday'] \
                and not data['wednesday'] \
                and not data['thursday'] \
                and not data['friday'] \
                and not data['saturday'] \
                and not data['sunday']:
            raise serializers.ValidationError({"monday": "you must enable at least one day of the week",
                                               "tuesday": "you must enable at least one day of the week",
                                               "wednesday": "you must enable at least one day of the week",
                                               "thursday": "you must enable at least one day of the week",
                                               "friday": "you must enable at least one day of the week",
                                               "saturday": "you must enable at least one day of the week",
                                               "sunday": "you must enable at least one day of the week",
                                               })
        return data

    class Meta:
        model = AlarmClock
        fields = '__all__'
