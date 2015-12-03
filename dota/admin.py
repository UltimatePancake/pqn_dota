from django.contrib import admin

# Register your models here.
from .models import Player, Match, Detail


class PlayerAdmin(admin.ModelAdmin):
    list_display = ('name', 'player_id')

admin.site.register(Player, PlayerAdmin)
admin.site.register(Match)
admin.site.register(Detail)
