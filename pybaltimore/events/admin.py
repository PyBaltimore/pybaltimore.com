from django.contrib import admin

from .models import LocalEvent


class LocalEventAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'date',
        'datetime',
        'hidden',
        'location',
    )
admin.site.register(LocalEvent, LocalEventAdmin)
