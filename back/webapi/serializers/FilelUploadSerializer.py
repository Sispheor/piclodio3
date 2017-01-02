from rest_framework import serializers

from webapi.models import BackupMusic


class FileUploadSerializer(serializers.ModelSerializer):
    backup_file = serializers.FileField()

    class Meta:
        model = BackupMusic
        fields = ('id', 'backup_file')
