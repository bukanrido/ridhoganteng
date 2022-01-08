from django.db import models

# mengambil table user
from django.contrib.auth.models import User

# Create your models here.
class Biodata(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nama = models.CharField(max_length=225)
    telp = models.CharField(max_length=20)
    alamat = models.TextField()

    def __str__(self):
        return "{} - {}". format(self.user,self.telp)

class API(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    api_key = models.CharField(max_length=255)

    def __str__(self):
        return self.user