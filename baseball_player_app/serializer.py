from rest_framework import serializers

from .models.player import Player
from .models.player_result import PlayerResult
from .models.player_batting_stats import PlayerBattingStats
from .models.player_pitching_stats import PlayerPitchingStats

class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = (
            'id',
            'no',
            'name',
            'position',
            'born',
            'age',
            'years',
            'height',
            'weight',
            'blood',
            'pi_pa',
            'place',
            'salary',
            'team',
            'info_year'
        )

class PlayerResultSerializer(serializers.ModelSerializer):

    player = PlayerSerializer()

    class Meta:
        model = PlayerResult
        fields = (
            'date',
            'stadium',
            'vs',
            'result_score',
            'win_lose',
            'position',
            'order',
            'avg',
            'at_bat',
            'hit',
            'hr',
            'rbi',
            'bb_hbp',
            'stolen_bases',
            'sacrifice_bunts',
            'sacrifice_flies',
            'strike_outs',
            'innings',
            'middle_score',
            'difference',
            'out_count',
            'first_runner',
            'second_runner',
            'third_runner',
            'ball_count',
            'strike_count',
            'result',
            'player'
        )

class PlayerBattingStatsSerializer(serializers.ModelSerializer):

    player = PlayerSerializer()

    class Meta:
        model = PlayerBattingStats
        fields = (
            'player',
            'year',
            'avg',
            'game',
            'plate_appearances',
            'at_bats',
            'runs_scored',
            'hits',
            'two_base_hits',
            'three_base_hits',
            'home_runs',
            'total_bases',
            'runs_batted_in',
            'stolen_bases',
            'caught_stealing',
            'sacrifice_bunts',
            'sacrifice_flies',
            'bases_on_balls',
            'intentional_walk',
            'hit_by_pitch',
            'strike_outs',
            'double_plays',
            'on_base_percentage',
            'slugging_percentage'
        )

class PlayerPitchingStatsSerializer(serializers.ModelSerializer):

    player = PlayerSerializer()

    class Meta:
        model = PlayerPitchingStats
        fields = (
            'player',
            'year',
            'earned_run_average',
            'game',
            'wins',
            'losses',
            'saves',
            'holds',
            'hold_points',
            'complete_games',
            'shoutout',
            'no_walks',
            'win_percentage',
            'batters_faced',
            'innings_pitched',
            'hits',
            'home_runs',
            'bases_on_balls',
            'intentional_walk',
            'hit_by_pitch',
            'strike_outs',
            'wild_pitches',
            'balks',
            'runs_allowed',
            'earned_runs_allowed'
        )