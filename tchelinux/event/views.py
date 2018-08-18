from django.shortcuts import render

from tchelinux.event.models import Event


def events(request):
    return render(request, 'event/list.html', {'object_list': Event.objects.all()})
