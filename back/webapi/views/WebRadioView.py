from django.http import Http404
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from webapi.models import WebRadio
from webapi.serializers.WebRadioSerializer import WebRadioSerializer


class WebRadioList(APIView):
    permission_classes = (AllowAny,)
    serializer_class = WebRadioSerializer

    def get(self, request, format=None):
        webradios = WebRadio.objects.all()
        serializer = WebRadioSerializer(webradios, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = WebRadioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class WebRadioDetail(APIView):
    """
    Retrieve, update or delete a WebRadio instance.
    """
    def get_object(self, pk):
        try:
            return WebRadio.objects.get(pk=pk)
        except WebRadio.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        webradio = self.get_object(pk)
        serializer = WebRadioSerializer(webradio)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        webradio = self.get_object(pk)
        serializer = WebRadioSerializer(webradio, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        webradio = self.get_object(pk)
        webradio.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
