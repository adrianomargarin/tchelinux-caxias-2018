from django.contrib import admin

from tchelinux.subscription.models import Subscription


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):

    exclude = ['deleted_at']
    list_display = ['id', 'fullname', 'created_at']
    list_display_links = ['id', 'fullname']
