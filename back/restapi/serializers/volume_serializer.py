

from rest_framework import serializers


class VolumeSerializer(serializers.Serializer):

    volume = serializers.IntegerField(min_value=0, max_value=100)

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass
