from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class Prompt(models.Model):
    category_choices = (
        ('Word','Word'),
        ('Movie', 'Movie'),
        ('Name', 'Name'),
        ('Acronym', 'Acronym'),
        ('Law', 'Law'),
    )

    word = models.CharField(max_length = 20)
    definition = models.CharField(max_length = 150)
    category = models.CharField(max_length=10,choices=category_choices,null=True, blank=True)

    def __str__(self):
        return str(self.word)


class UserDefinition(models.Model):
    room = models.CharField(max_length=4)
    user_definition = models.CharField(max_length= 150)
    user_name = models.ForeignKey(User, blank=True,null=True)
    prompt = models.ForeignKey(Prompt)

    def __str__(self):
        return self.user_definition
