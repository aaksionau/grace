from django.shortcuts import render
from django.template.loader import get_template
import json
import os

from .models import Gallery, Photo
from pages.models import Page

def galleries(request):
    galleries = Gallery.objects.all()
    data = Page.objects.get(alias='galleries')
    return render(request, 'photos/base.html', {'galleries': galleries, 'data':data})

def gallery(request, gallery_alias):
    gallery = Gallery.objects.get(alias=gallery_alias)
    photos = Photo.objects.filter(gallery__alias=gallery_alias)
    return render(request, 'photos/detail.html', {'gallery': gallery, 'photos': photos})

def import_photos(request):
    path_to_photos = 'F:\Aliaksei\Downloads\iloveimg-resized'
    phs = []
    for photo in os.listdir(path_to_photos):
        ph = Photo()
        ph.image = f"photos/prayer-blessings-kids-2018/{photo}"
        ph.thumbnail = f"photos/prayer-blessings-kids-2018/minified/{photo}"
        ph.gallery = Gallery.objects.get(pk=9)
        ph.save()
   
    return render(request, 'photos/import.html', {'photos':phs})