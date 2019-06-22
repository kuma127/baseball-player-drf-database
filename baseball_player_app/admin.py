from django.contrib import admin
from import_export import resources, fields
from import_export.admin import ImportExportModelAdmin
from import_export.widgets import Widget

from .models.player import Player
from .models.player_result import PlayerResult

admin.site.register(PlayerResult)

class PlayerResource(resources.ModelResource):

    class Meta:
        model = Player
    
    
    fields = ('no', 'name', 'position', 'born', 'age', 'years', 'height', 'weight', 'blood', 'pi_pa', 'place', 'salary', 'team', 'info_year')
    export_order = ('no', 'name', 'position', 'born', 'age', 'years', 'height', 'weight', 'blood', 'pi_pa', 'place', 'salary', 'team', 'info_year')

@admin.register(Player)
class PlayerAdmin(ImportExportModelAdmin):
    resource_class = PlayerResource
