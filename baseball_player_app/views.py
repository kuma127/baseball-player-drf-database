import csv
import io
import urllib

from django_filters import rest_framework as filters
from rest_framework import viewsets

from .models.player import Player
from .models.player_result import PlayerResult
from .serializer import PlayerSerializer, PlayerResultSerializer

class PlayerFilter(filters.FilterSet):

    no = filters.NumberFilter(lookup_expr='gt')
    name = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Player
        fields = ['no', 'name']

class PlayerViewSet(viewsets.ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
    filter_class = PlayerFilter

class PlayerResultFilter(filters.FilterSet):

    date = filters.DateFilter()
    date_range = filters.DateFromToRangeFilter(field_name='date')
    player__name = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = PlayerResult
        fields = ['date', 'player']

class PlayerResultViewSet(viewsets.ModelViewSet):
    queryset = PlayerResult.objects.all()
    serializer_class = PlayerResultSerializer
    filter_class = PlayerResultFilter