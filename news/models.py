from django.db import models


# Create your models here.

class New(models.Model):
    title = models.CharField(max_length=400, default='')
    content = models.TextField(max_length=1000, default='')
