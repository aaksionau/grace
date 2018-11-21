from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^future-events/$', views.events, name='events'),
    url(r'^future-events/(?P<event_id>[0-9]+)/$', views.event, name='event'),
    url(r'^news/$', views.news, name='news'),
    url(r'^news/(?P<event_id>[0-9]+)/$', views.event, name='news_item'),
]