from django.db import models


class BackupFile(models.Model):
    backup_file = models.FileField(upload_to="backup_mp3")
