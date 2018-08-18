from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404

from django.urls import reverse_lazy

from tchelinux.event.models import Event
from tchelinux.subscription.forms import SubscriptionForm


def subscriptions(request, event_pk):
    event = get_object_or_404(Event, pk=event_pk)
    form = SubscriptionForm()

    if request.method == 'POST':
        form = SubscriptionForm(request.POST)

        if form.is_valid():
            form.instance.event = event
            form.save()

            return redirect(reverse_lazy('home'))

    context = {
        'form': form
    }

    return render(request, 'subscription/form.html', context)
