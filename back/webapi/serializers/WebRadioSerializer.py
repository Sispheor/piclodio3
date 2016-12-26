from rest_framework import serializers

from webapi.models import WebRadio


class WebRadioSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True, allow_blank=False, max_length=250)
    url = serializers.CharField(required=True, allow_blank=False, max_length=250)
    is_default = serializers.BooleanField(read_only=True)

    class Meta:
        model = WebRadio
        fields = ('id', 'name', 'url', 'is_default')
