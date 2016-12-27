from rest_framework import serializers

from webapi.models import WebRadio


class PlayerManagerSerializer(serializers.Serializer):
    status = serializers.CharField()
    webradio = serializers.PrimaryKeyRelatedField(required=False,
                                                  queryset=WebRadio.objects.all(),
                                                  allow_empty=True)

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass



