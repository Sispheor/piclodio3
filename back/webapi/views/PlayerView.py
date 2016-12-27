from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from webapi.models import Player, WebRadio
from webapi.serializers.PlayerSerializer import PlayerManagerSerializer


class PlayerStatus(APIView):
    permission_classes = (AllowAny,)
    # serializer_class = PlayerManagerSerializer

    def get(self, request, format=None):
        """
        Get the Mplayer status
        """
        if Player.is_started():
            status = "on"
        else:
            status = "off"

        answer = {
            "status": status
        }
        return Response(answer)

    def post(self, request, format=None):
        serializer = PlayerManagerSerializer(data=request.data)

        if serializer.is_valid():
            new_status = serializer.validated_data["status"]
            if new_status == "on":
                if "webradio" in serializer.validated_data:
                    webradio = serializer.validated_data["webradio"]
                    url_to_play = webradio.url
                else:
                    # get the default web radio
                    default_web_radio = WebRadio.objects.get(is_default=True)
                    url_to_play = default_web_radio.url

                Player.play(url_to_play)
                returned_status = "on"
            else:
                Player.stop()
                returned_status = "off"

            answer = {
                "status": returned_status
            }
            return Response(answer)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
