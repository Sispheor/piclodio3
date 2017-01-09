from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from webapi.Utils.SoundManager import SoundManager
from webapi.serializers.SoundManagerSerializer import SoundManagerSerializer


class VolumeManagement(APIView):
    permission_classes = (AllowAny,)

    def get(self, request):
        """
        Get the volume status
        """
        content = {'volume': SoundManager.get_volume()}
        return Response(content)

    def post(self, request):
        serializer = SoundManagerSerializer(data=request.data)

        if serializer.is_valid():
            SoundManager.set_volume(serializer.validated_data["volume"])
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
