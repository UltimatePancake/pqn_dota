from django.contrib import admin

# Register your models here.
from .models import Player
from .models import Match
from .models import Detail

admin.site.register(Player)
admin.site.register(Match)
admin.site.register(Detail)
