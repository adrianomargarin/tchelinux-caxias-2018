from django import forms

from tchelinux.subscription.models import Subscription


class SubscriptionForm(forms.ModelForm):

    class Meta:
        model = Subscription
        fields = ['fullname', 'email']
