from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from restapi.models.volume import Volume
from restapi.serializers.volume_serializer import VolumeSerializer
from utils.sound_manager import SoundManager


class VolumeView(APIView):
    @swagger_auto_schema(
        responses={
            '200': VolumeSerializer(),
        },
        operation_id='Get volume',
        operation_description='Get current volume'
    )
    def get(self, request):
        """
        Get the volume status
        """
        volume = Volume()
        serializer = VolumeSerializer(volume)

        return Response(serializer.data)

    @swagger_auto_schema(
        responses={
            '200': VolumeSerializer(),
            '400': "Bad request"
        },
        operation_id='Set volume',
        operation_description='Set new volume level'
    )
    def post(self, request):
        serializer = VolumeSerializer(data=request.data)

        if serializer.is_valid():
            SoundManager.set_volume(serializer.validated_data["volume"])
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
