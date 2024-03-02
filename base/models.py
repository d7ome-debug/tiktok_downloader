# models.py
from django.db import models

class Video(models.Model):
    url = models.URLField()
