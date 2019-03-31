
os.environ.setdefault("DJANGO_SETTINGS_MODULE","baseball_player_drf_database.settings")
 
django.setup()

from baseball_player_app.models.player import Player

player = Player.objects.get(id=1)
print(player.name)
