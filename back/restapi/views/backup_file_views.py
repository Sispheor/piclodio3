import os

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from restapi.models.backup_file import BackupFile
from restapi.serializers.backup_file_serializer import BackupFileSerializer


class BackupFileView(APIView):

    def get(self, request):
        backup_file = BackupFile.objects.all()
        serializer = BackupFileSerializer(backup_file, many=True)
        return Response(serializer.data)

    # curl -X POST -F "backup_file=@/home/nico/Desktop/blues_song.mp3" http://127.0.0.1:8000/api/backup/
    def post(self, request):
        serializer = BackupFileSerializer(data=request.data)

        if serializer.is_valid():
            # delete the existing MP3 file if exist
            backup_files = BackupFile.objects.all()
            for el in backup_files:
                os.remove(el.backup_file.path)
                el.delete()
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
