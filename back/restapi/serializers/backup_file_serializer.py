from django.core.validators import FileExtensionValidator
from rest_framework import serializers

from restapi.models.backup_file import BackupFile


class BackupFileSerializer(serializers.ModelSerializer):
    backup_file = serializers.FileField(validators=[FileExtensionValidator(
                                       allowed_extensions=['mp3', 'wav', 'mp4', 'wmv'])])

    class Meta:
        model = BackupFile
        fields = '__all__'
