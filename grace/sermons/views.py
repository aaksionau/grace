import datetime

from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

import requests
import json

from django.http import JsonResponse
from sermons.models import Sermon, Biblebook, Preacher
from pages.models import Page

def sermons(request):

    bible_book_id = int(request.GET.get('bible_book', "0"))
    preacher_id = int(request.GET.get('preacher', "0"))

    sermons_list = Sermon.objects.all().order_by('-date')

    bible_books = [
        book_id['bible_book_id'] for book_id in sermons_list.values('bible_book_id')
    ]

    if bible_book_id > 0:
        sermons_list = sermons_list.filter(bible_book_id=bible_book_id)

    if preacher_id > 0:
        sermons_list = sermons_list.filter(preacher_id=preacher_id)

    paginator = Paginator(sermons_list, 5)

    page = request.GET.get('page')


    print(bible_books)
    bible_books = Biblebook.objects.filter(id__in = bible_books).order_by('order')
    preachers = Preacher.objects.all().order_by('last_name')


    data = Page.objects.get(alias="sermons")

    try:
        sermons = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        sermons = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        sermons = paginator.page(paginator.num_pages)

    return render(request, 'sermons/base.html', {'sermons': sermons, 'bible_books': bible_books, 'preachers': preachers, 'data':data, 'selected_preacher_id': preacher_id, 'selected_bible_book_id':bible_book_id}, RequestContext(request))

def sermon(request, pk):
    sermon_data = Sermon.objects.get(pk=pk)

    return render(request, 'sermons/sermon-detail.html', {'sermon': sermon_data, 'data':sermon_data})

def feed(request):
    response = render_to_response(
        'sermons/feed.xml', {'entries': Sermon.objects.all(), })
    response['Content-Type'] = 'application/rss+xml;'
    return response

def update_sermons(request):
    response = requests.get('http://grace.kharkov.ua/static/media/sermons/sermon_to_update.json')
    response.encoding = 'utf-8'
    data = response.json()
    
    date_arr = [int(n) for n in data['date'].split('.')]
    sermon = Sermon()
    sermon.title = data['title']
    sermon.audio = data['audio']
    sermon.bible_book = Biblebook.objects.get(title__icontains=data['album'])
    last_name = data['artist'].split(' ')[1]

    sermon.date = datetime.datetime(date_arr[2], date_arr[1], date_arr[0], 10, 0, 0)

    sermon.preacher = Preacher.objects.get(last_name=last_name)
    sermon.chapter_and_verses = data['comment']

    sermon.save()
    
    return JsonResponse({'id':sermon.id})