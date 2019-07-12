from django.db import models
from .player import Player

class PlayerBattingStats(models.Model):

    class Meta:
        db_table = 'player_batting_stats'
    
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    year = models.IntegerField(default=0)
    avg = models.DecimalField(max_digits=4, decimal_places=3, default=0.000)
    game = models.IntegerField(default=0)
    plate_appearances = models.IntegerField(default=0)
    at_bats = models.IntegerField(default=0)
    runs_scored = models.IntegerField(default=0)
    hits = models.IntegerField(default=0)
    two_base_hits = models.IntegerField(default=0)
    three_base_hits = models.IntegerField(default=0)
    home_runs = models.IntegerField(default=0)
    total_bases = models.IntegerField(default=0)
    runs_batted_in = models.IntegerField(default=0)
    stolen_bases = models.IntegerField(default=0)
    caught_stealing = models.IntegerField(default=0)
    sacrifice_bunts = models.IntegerField(default=0)
    sacrifice_flies = models.IntegerField(default=0)
    bases_on_balls = models.IntegerField(default=0)
    intentional_walk = models.IntegerField(default=0)
    hit_by_pitch = models.IntegerField(default=0)
    strike_outs = models.IntegerField(default=0)
    double_plays = models.IntegerField(default=0)
    on_base_percentage = models.DecimalField(max_digits=4, decimal_places=3, default=0.000)
    slugging_percentage = models.DecimalField(max_digits=4, decimal_places=3, default=0.000)