from django.db import models
from .player import Player

class PlayerPitchingStats(models.Model):

    class Meta:
        db_table = 'player_pitching_stats'
      
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    year = models.IntegerField(default=0)
    earned_run_average = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
    game = models.IntegerField(default=0)
    wins = models.IntegerField(default=0)
    losses = models.IntegerField(default=0)
    saves = models.IntegerField(default=0)
    holds = models.IntegerField(default=0)
    hold_points = models.IntegerField(default=0)
    complete_games = models.IntegerField(default=0)
    shoutout = models.IntegerField(default=0)
    no_walks = models.IntegerField(default=0)
    win_percentage = models.DecimalField(max_digits=4, decimal_places=3, default=0.000)
    batters_faced = models.IntegerField(default=0)
    innings_pitched = models.DecimalField(max_digits=5, decimal_places=1, default=0.0)
    hits = models.IntegerField(default=0)
    home_runs = models.IntegerField(default=0)
    bases_on_balls = models.IntegerField(default=0)
    intentional_walk = models.IntegerField(default=0)
    hit_by_pitch = models.IntegerField(default=0)
    strike_outs = models.IntegerField(default=0)
    wild_pitches = models.IntegerField(default=0)
    balks = models.IntegerField(default=0)
    runs_allowed = models.IntegerField(default=0)
    earned_runs_allowed = models.IntegerField(default=0)
    