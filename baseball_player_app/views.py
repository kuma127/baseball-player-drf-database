import csv
import io
import urllib

import django_filters
from rest_framework import viewsets, filters

from .models.player import Player
from .models.player_result import PlayerResult
from .serializer import PlayerSerializer, PlayerResultSerializer


class PlayerViewSet(viewsets.ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer

class PlayerResultViewSet(viewsets.ModelViewSet):
    queryset = PlayerResult.objects.all()
    serializer_class = PlayerResultSerializer