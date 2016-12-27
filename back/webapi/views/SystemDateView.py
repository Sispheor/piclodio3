import json
from time import strftime

from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response


class SystemDateList(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, format=None):
        # get the local system date
        clock = strftime("%Y-%m-%dT%H:%M:%S")
        print clock

        return Response(str(clock))
