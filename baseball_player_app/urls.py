from rest_framework import routers
from .views import PlayerViewSet, PlayerResultViewSet, PlayerBattingStatsViewSet, PlayerPitchingStatsViewSet

app_name = 'baseball_player_app'

router = routers.DefaultRouter()
router.register(r'players', PlayerViewSet)
router.register(r'results', PlayerResultViewSet)
router.register(r'batting-stats', PlayerBattingStatsViewSet)
router.register(r'pitching-stats', PlayerPitchingStatsViewSet)