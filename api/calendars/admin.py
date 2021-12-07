from django.contrib import admin

from . import models

# Register your models here.
# admin.site.register(models.Event)

# v2

@admin.register(models.Event)
class EventAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'date_start',
        'date_end',
        'time_start',
        'time_end',
    ]
    fields = ('title', 'description', 'date_start', 'date_end', 'time_start', 'time_end', 'guests', 'created_by',)
    filter_horizontal = ('guests',)

admin.site.register(models.Invite)


