from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.sermons, name='sermons'),
    #url(r'^imports/$', views.imports, name='imports'),
    url(r'^(?P<pk>[0-9]+)/$', views.sermon, name='sermon'),
    url(r'^feed/$', views.feed, name='feed'),
    url(r'^update-sermons/', views.update_sermons, name='update-sermons')
]