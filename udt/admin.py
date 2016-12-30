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
admin.site.register(Dispatcher, DispatcherAdmin)
