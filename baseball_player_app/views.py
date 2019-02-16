import csv
import io
import urllib

import django_filters
from rest_framework import viewsets, filters

from .models.player import Player
from .serializer import PlayerSerializer


class PlayerViewSet(viewsets.ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
