from django.db import models
from .player import Player

class BattingResult(models.Model):

    class Meta:
        db_table = 'batting_result'
    
    player_id = models.ForeignKey(Player, on_delete=models.PROTECT)
    