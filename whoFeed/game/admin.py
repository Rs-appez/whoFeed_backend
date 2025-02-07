from django.contrib import admin

from .models import Champion, Tag, ParType

admin.site.register(Champion)
admin.site.register(Tag)
admin.site.register(ParType)
