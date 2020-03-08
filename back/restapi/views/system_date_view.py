from drf_yasg.utils import swagger_auto_schema
from rest_framework.views import APIView
from rest_framework.response import Response

from restapi.models.clock import Clock
from restapi.serializers.clock_serializer import ClockSerializer


class SystemDateView(APIView):
    @swagger_auto_schema(
        responses={
            '200': ClockSerializer(),
        },
        operation_id='Clock',
        operation_description='Get current system date et time'
    )
    def get(self, request):

        clock = Clock()
        serializer = ClockSerializer(clock)

        return Response(serializer.data)
