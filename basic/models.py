from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from django.urls import reverse


class Funeral(AbstractUser):
    adress1 = models.CharField(max_length=100)
    adress2 = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    post_code = models.SmallIntegerField()
    nip = models.IntegerField()
    krs = models.IntegerField()
    regon = models.IntegerField()
    service_info = models.CharField(max_length=1000)
    equipment = models.CharField(max_length=1000)

    REQUIRED_FIELDS = ['email', 'adress1', 'adress2', 'city', 'post_code', 'nip', 'krs', 'regon']
    objects = UserManager()

    def get_absolute_url(self):
        return reverse("comp details", kwargs={"id": self.id})


class Obit(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    cemetery_name = models.CharField(max_length=100)
    cemetery_address = models.CharField(max_length=300)
    church_name = models.CharField(max_length=100)
    church_address = models.CharField(max_length=300)
    born_date = models.DateField()
    death_date = models.DateField()
    description = models.CharField(max_length=2000)

    def __str__(self):
        return self.first_name.capitalize() + self.last_name.capitalize() + str(self.id)

    def get_absolute_url(self):
        return reverse("obits details", kwargs={"id": self.id})

    class Meta:
        ordering = ['-death_date']






