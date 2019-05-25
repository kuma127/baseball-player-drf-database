from django.db import models
from django.utils import timezone
from .player import Player

class PlayerResult(models.Model):

    class Meta:
        db_table = 'player_result'
    
    date = models.DateField(default=timezone.now)
    stadium = models.CharField(max_length=255)
    vs = models.CharField(max_length=255)
    result_score = models.CharField(max_length=255)
    win_lose = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    order = models.IntegerField(default=0)
    avg = models.DecimalField(max_digits=4, decimal_places=3, default=0.000)
    at_bat = models.IntegerField(default=0)
    hit = models.IntegerField(default=0)
    hr = models.IntegerField(default=0)
    rbi = models.IntegerField(default=0)
    bb_hbp = models.IntegerField(default=0)
    stolen_bases = models.IntegerField(default=0)
    sacrifice_bunts = models.IntegerField(default=0)
    sacrifice_flies = models.IntegerField(default=0)
    strike_outs = models.IntegerField(default=0)
    innings = models.CharField(max_length=255)
    middle_score = models.CharField(max_length=255)
    difference = models.CharField(max_length=255)
    out_count = models.CharField(max_length=255)
    first_runner = models.CharField(max_length=255)
    second_runner = models.CharField(max_length=255)
    third_runner = models.CharField(max_length=255)
    ball_count = models.CharField(max_length=255)
    strike_count = models.CharField(max_length=255)
    result = models.CharField(max_length=255)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    