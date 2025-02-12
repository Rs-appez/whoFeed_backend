from django.contrib import admin

from .models import Champion, Tag, ParType, Player


class PlayerAdmin(admin.ModelAdmin):
    readonly_fields = ("jwttoken", "id")


admin.site.register(Champion)
admin.site.register(Tag)
admin.site.register(ParType)
admin.site.register(Player, PlayerAdmin)
