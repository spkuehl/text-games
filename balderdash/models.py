from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

class Comments(models.Model):
    user = models.ForeignKey(User)
    text = models.CharField(max_length=255)

class Prompt(models.Model):
    word = models.CharField(max_length = 20)
    definition = models.CharField(max_length = 150)
    category = models.IntegerField(null=True, blank=True)
    def __str__(self):
        return str(self.word)
