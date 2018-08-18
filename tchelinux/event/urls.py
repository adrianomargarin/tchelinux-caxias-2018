from django.urls import path

from tchelinux.event.views import events

app_name = 'event'


urlpatterns = [
    path('', events, name='list'),
]
