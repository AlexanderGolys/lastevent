from django.db import models
from django.contrib.auth.models import AbstractUser


class Funeral(AbstractUser):
    adress1 = models.CharField(max_length=100)
    adress2 = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    post_code = models.SmallIntegerField()
    nip = models.SmallIntegerField()
    krs = models.SmallIntegerField()
    regon = models.SmallIntegerField()
    service_info = models.CharField(max_length=1000)
    equipment = models.CharField(max_length=1000)
    REQUIRED_FIELDS = ['email', ]


