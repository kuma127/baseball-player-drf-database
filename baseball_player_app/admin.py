from django.contrib import admin
from import_export import resources, fields
from import_export.admin import ImportExportModelAdmin
from import_export.widgets import Widget

from .models.player import Player

class PlayerResource(resources.ModelResource):

    class Meta:
        model = Player
        # ここに、CSVにIdがなくても自動生成してくれるような処理を追加する
    
    
    fields = ('no', 'name', 'position', 'born', 'age', 'years', 'height', 'weight', 'blood', 'pi_pa', 'place', 'salary')
    export_order = ('no', 'name', 'position', 'born', 'age', 'years', 'height', 'weight', 'blood', 'pi_pa', 'place', 'salary')

@admin.register(Player)
class PlayerAdmin(ImportExportModelAdmin):
    resource_class = PlayerResource
