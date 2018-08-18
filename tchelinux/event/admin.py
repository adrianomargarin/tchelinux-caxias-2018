from django.contrib import admin

from tchelinux.event.models import Event


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):

    exclude = ['deleted_at']
    list_display = ['id', 'title', 'start_date', 'end_date']
    list_display_links = ['id', 'title']
