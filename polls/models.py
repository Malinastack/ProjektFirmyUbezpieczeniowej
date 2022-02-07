from django.db import models

# Create your models here.
from django.db import models


class Klient(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)


class Ziemniak(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
