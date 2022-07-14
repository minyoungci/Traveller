from django.db import models

# Create your models here.


class Maps(models.Model):
    name = models.CharField(max_length=50, default=True)
