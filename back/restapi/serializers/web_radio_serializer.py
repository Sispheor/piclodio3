from rest_framework import serializers

from restapi.models.web_radio import WebRadio


class WebRadioSerializer(serializers.ModelSerializer):
    class Meta:
        model = WebRadio
        fields = '__all__'
