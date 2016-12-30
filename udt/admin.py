from django.contrib import admin
from .models import Dispatcher


class DispatcherAdmin(admin.ModelAdmin):
    list_display = (
        'uid',
        'filter_by_tool',
        'assign_to',
        'task_received',
        'task',
        'subject',
    )
    list_filter = (
        'filter_by_tool',
        'task_received',
        'assign_to',
        'geo',
    )
    search_fields = (
        'task',
        'subject',
        'description',
    )
    raw_id_fields = (
        ('assign_to',)
    )
    date_hierarchy = (
        'task_received'
    )
    ordering = (
        ['task', 'task_received']
    )
admin.site.register(Dispatcher, DispatcherAdmin)
