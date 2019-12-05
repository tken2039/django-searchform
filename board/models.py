# board/models.py

from django.db import models
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    tags = models.CharField(max_length=255)

    def __str__(self):
        return self.title