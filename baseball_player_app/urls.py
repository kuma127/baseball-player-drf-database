from rest_framework import routers
from .views import PlayerViewSet

app_name = 'baseball_player_app'

router = routers.DefaultRouter()
router.register(r'players', PlayerViewSet)
