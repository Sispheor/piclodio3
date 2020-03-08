from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from restapi.models import WebRadio
from restapi.serializers.player_serializer import PlayerSerializer
from restapi.serializers.web_radio_serializer import WebRadioSerializer
from utils.player_manager import PlayerManager


class PlayerStatus(APIView):

    @swagger_auto_schema(
        responses={
            '200': PlayerSerializer,
            '400': "Bad Request"
        },
        security=[],
        operation_id='Player status',
        operation_description='Get the status of the player'
    )
    def get(self, request):
        """
        Get the player status
        """
        player_manager = PlayerManager()

        try:
            default_web_radio = WebRadio.objects.get(is_default=True)
        except WebRadio.DoesNotExist:
            default_web_radio = None

        answer = {
            "active": player_manager.is_started(),
            "webradio": "no default web radio yet",
        }

        if default_web_radio is not None:
            answer["webradio"] = WebRadioSerializer(default_web_radio).data

        return Response(answer)

    @swagger_auto_schema(
        request_body=PlayerSerializer,
        responses={
            '200': PlayerSerializer,
            '400': "Bad Request"
        },
        security=[],
        operation_id='Player control',
        operation_description='Switch the status of the player'
    )
    def post(self, request):
        serializer = PlayerSerializer(data=request.data)
        player_manager = PlayerManager()
        if serializer.is_valid():
            active = serializer.validated_data["active"]
            if active:
                # give a web radio to play is optional
                if "webradio" in serializer.validated_data:
                    webradio = serializer.validated_data["webradio"]
                    url_to_play = webradio.url
                    # remove the is_default from other web radio
                    qs = WebRadio.objects.filter(is_default=True)
                    qs.update(is_default=False)
                    # the selected web radio become the default one
                    webradio.is_default = True
                    webradio.save()
                    playing_webradio = webradio
                else:
                    # get the default web radio if exist
                    try:
                        default_web_radio = WebRadio.objects.get(is_default=True)
                        url_to_play = default_web_radio.url
                        playing_webradio = default_web_radio
                    except WebRadio.DoesNotExist:
                        # No default web radio
                        answer = {
                            "status": "error, no default web radio. Please specify one"
                        }
                        return Response(answer, status=status.HTTP_400_BAD_REQUEST)

                player_manager.threaded_start(url_to_play)
                answer = {
                    "active": True,
                    "webradio": WebRadioSerializer(playing_webradio).data,
                }
                return Response(answer)

            else:
                player_manager.stop()
                answer = {
                    "active": False
                }
                return Response(answer)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
