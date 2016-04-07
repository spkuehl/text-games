from __future__ import unicode_literals

from django.db import models

class Prompt(models.Model):
    word = models.CharField(max_length = 20)
    definition = models.CharField(max_length = 150)
    category = models.IntegerField(null=True, blank=True)
    def __str__(self):
        return str(self.word)
