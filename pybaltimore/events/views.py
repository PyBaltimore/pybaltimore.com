from django.shortcuts import render
from django.utils import timezone

from .models import LocalEvent


def events_list(request):
    events = LocalEvent.objects.filter(hidden=False,
                                       date__gte=timezone.now().date()).order_by("datetime", 'date')
    context = {
        'events': events,
    }
    return render(request, 'events/events_list.html', context=context)


def about(request):
    return render(request, 'events/about.html')
