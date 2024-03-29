from django.db import models

# Create your models here.
class Lobby(models.Model):
    #lobby_id = models.CharField(max_length=50, unique=True)
    lobby_name = models.CharField(max_length=50, unique=True)
    num_players = models.IntegerField(default=4) 
    game_mode = models.CharField(max_length=100, default='Floyd')  
    privacy = models.CharField(max_length=20, default='public') 
    playersJoined = models.IntegerField(default=1)
    def __str__(self):
        return self.lobby_id

class LinesForTyping (models.Model):
    Character = models.CharField(max_length=25)
    Line = models.TextField()

    class Meta:
        app_label = 'trollapp'

