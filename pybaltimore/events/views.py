from django.shortcuts import render
from django.utils import timezone

from .models import LocalEvent


def events_list(request):
    events = LocalEvent.objects.filter(hidden=False,
                                       date__gte=timezone.now().date()).order_by('date')
    context = {
        'events': _sort_events_into_days(events),
    }
    return render(request, 'events/events_list.html', context=context)


def about(request):
    return render(request, 'events/about.html')


def _sort_events_into_days(event_list):
    """
    Given a list of events, group it into a list of tuples with the first
    tuple value being the date and the second tuple value being a list of
    events for that day.
    """
    result = []
    events_to_days = {}
    for event in event_list:
        if not event.date in events_to_days:
            events_to_days[event.date] = [event,]
        else:
            events_to_days[event.date].append(event)
    for key in sorted(events_to_days.keys(), reverse=True):
        result.append((key, events_to_days[key]))
    return result
