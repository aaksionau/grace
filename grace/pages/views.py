from django.shortcuts import render, get_object_or_404, render_to_response
from django.template import RequestContext
from django.template.loader import get_template
from django.core.mail import EmailMessage
from datetime import date

from .forms import ContactsForm
from .models import Page
from photos.models import Gallery
from sermons.models import Sermon
from events.models import Event, ScheduleEvent, WEEKDAY_NAMES


def index(request):
    homeBody = Page.objects.get(alias="home")
    galleries = Gallery.objects.filter().order_by('created')[:2]
    sermons = Sermon.objects.all().order_by('-date')[:3]
    schedule_events = ScheduleEvent.objects.all().order_by('event_day', 'time')

    schedule_events = put_weekday(schedule_events)

    events = Event.objects.filter(date__gte=date.today(), published=True, event_type='future_events').order_by('-date')[0:3]
    news = Event.objects.filter(date__lte=date.today(), published=True, event_type='news').order_by('-date')[0:3]

    return render(request, 'pages/home.html', {
        'data': homeBody,
        'galleries': galleries,
        'sermons': sermons,
        'events': events,
        'news': news,
        'schedule_events': schedule_events})

def put_weekday(schedule_evs):
    for event in schedule_evs:
        event.event_day = WEEKDAY_NAMES[event.event_day][1]
    return schedule_evs

def page(request, parent_alias="home", child_alias=""):

    selected_alias = ""
    if not child_alias:
        selected_alias = parent_alias
    else:
        selected_alias = child_alias

    data = get_object_or_404(Page, alias=selected_alias)

    return render(request, 'pages/page.html', {'data': data})

def sitemap(request):
    return render(request, 'pages/sitemap.xml', {'pages': Page.objects.all()})


def contacts(request):
    data = Page.objects.get(alias='contacts')
    if request.method == 'POST':
        contacts_data = ContactsForm(request.POST)
        if contacts_data.is_valid():
            contacts_data.save()
            send_feedback(contacts_data)
            return render(request, 'pages/contacts.html', {'thankyou': 'Спасибо за ваше сообщение. Мы ответим вам в течение нескольких дней.', 'data': data})
        else:
            return render(request, 'pages/contacts.html', {'form': contacts_data, 'data': data})
    else:
        contacts_data = ContactsForm()
        return render(request, 'pages/contacts.html', {'form': contacts_data, 'data': data})


def send_feedback(contacts_data):
    subject, from_email, to_email = 'Новое сообщение с сайта', 'Admin <admin@paloni.webfactional.com>', [
        'Aliaksei Aksionau <alexei.aksenov@gmail.com>']
    ctxt = {'email': contacts_data.cleaned_data['email'],
            'name': contacts_data.cleaned_data['name'], 'body': contacts_data.cleaned_data['body']}
    body = get_template(
        'letters/feedback.html').render({'feedback': ctxt})
    msg = EmailMessage(subject, body, from_email, to_email)
    msg.content_subtype = "html"
    msg.send()

def twr(request):
    page = Page.objects.get(alias='twr')
    return render(request, 'pages/twr.html', {'data':page})

def handler404(request):
    page = Page.objects.get(alias='404')
    response = render_to_response('pages/error.html', {'data': page})
    response.status_code = 404
    return response

def handler500(request):
    page = Page.objects.get(alias='500')
    response = render_to_response('pages/error.html', {'data':page})
    response.status_code = 500
    return response
