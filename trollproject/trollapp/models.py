from django.db import models

# Create your models here.

class LinesForTyping (models.Model):
    Character = models.CharField(max_length=25)
    Line = models.TextField()
    class Meta:
        app_label = 'trollapp'