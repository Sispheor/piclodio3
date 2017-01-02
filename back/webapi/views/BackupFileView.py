import os

from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from webapi.models import BackupMusic
from webapi.serializers.FilelUploadSerializer import FileUploadSerializer

# curl -X POST -F "image=@/home/nico/Desktop/backup.mp3" http://127.0.0.1:8000/backup
class BackupFileView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request):
        backup_file = BackupMusic.objects.all()
        serializer = FileUploadSerializer(backup_file, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = FileUploadSerializer(data=request.data)

        if serializer.is_valid():
            # delete the existing MP3 file if exist
            backup_files = BackupMusic.objects.all()
            for el in backup_files:
                os.remove(el.backup_file.path)
                el.delete()
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)