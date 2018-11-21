from django.shortcuts import render
from datetime import date
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from pages.models import Page
from .models import Event


def events(request):
    page_data = Page.objects.get(alias="future-events")
    events = Event.objects.filter(published=True, event_type="future_events").order_by('-date')

    paginator = Paginator(events, 5)
    page = request.GET.get('page')

    try:
        events = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        events = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        events = paginator.page(paginator.num_pages)

    return render(request, 'events/base.html', {'events': events, 'data': page_data})

def news(request):
    page_data = Page.objects.get(alias="news")
    news = Event.objects.filter(published=True, event_type="news").order_by('-date')

    paginator = Paginator(news, 5)
    page = request.GET.get('page')

    try:
        news = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        news = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        news = paginator.page(paginator.num_pages)


    return render(request, 'events/base.html', {'events': news, 'data': page_data})

def event(request, event_id):
    event_data = Event.objects.get(pk=event_id)
    page_data = Page.objects.get(alias=event_data.event_type.replace('_', '-'))
    page_data.title = event_data.title + ' - ' + page_data.title
    return render(request, 'events/event.html', {'event': event_data, 'data': page_data})
