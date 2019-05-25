from rest_framework import serializers

from .models.player import Player
from .models.player_result import PlayerResult

class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = (
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
            'salary')

class PlayerResultSerializer(serializers.ModelSerializer):
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