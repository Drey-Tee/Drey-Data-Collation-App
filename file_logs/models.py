from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class UploadFile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    file_name = models.CharField(max_length=200)
    file = models.FileField(upload_to='files')
    uploaded_at = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return f'{self.file_name} UploadFile'


class AllData(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.ForeignKey(UploadFile, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    age = models.CharField(max_length=200)
    gender = models.CharField(max_length=200)
    address = models.CharField(max_length=200)

