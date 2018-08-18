from django.urls import path

from tchelinux.subscription.views import subscriptions

app_name = 'subscription'


urlpatterns = [
    path('evento/<int:event_pk>', subscriptions, name='form'),
]
