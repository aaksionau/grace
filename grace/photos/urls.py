from django.conf.urls import url, include
from django.conf.urls.static import static
from . import views

urlpatterns = [
    url(r'^galleries/$', views.galleries, name='galleries'),
    url(r'^galleries/import/$', views.import_photos, name='import'),
    url(r'^galleries/(?P<gallery_alias>[\w-]+)/$', views.gallery, name='gallery'),
]