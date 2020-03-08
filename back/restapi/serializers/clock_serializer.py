from time import strftime

from rest_framework import serializers


class ClockSerializer(serializers.Serializer):

    clock = serializers.CharField(default=strftime("%Y-%m-%dT%H:%M:%S"))

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass
