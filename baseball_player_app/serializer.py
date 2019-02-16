from rest_framework import serializers

from .models.player import Player

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