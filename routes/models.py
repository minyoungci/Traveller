from django.db import models
from . import models

# Create your models here.


class Maps(models.Model):
    name = models.CharField(max_length=50, default=True)
    location = models.CharField(max_length=50, default=True)
