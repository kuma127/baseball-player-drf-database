import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE","test_project.settings")
import django
django.setup()

from baseball_player_app.models.player import Player

player = Player.objects.get(id=1)
print(player.name)
