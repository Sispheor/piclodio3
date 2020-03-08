from rest_framework import serializers

from restapi.models import WebRadio


class PlayerSerializer(serializers.Serializer):
    active = serializers.BooleanField()
    webradio = serializers.PrimaryKeyRelatedField(required=False,
                                                  queryset=WebRadio.objects.all(),
                                                  allow_empty=True)

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass
