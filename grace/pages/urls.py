from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^home/$', views.index, name='home_index'),
    url(r'^contacts/$', views.contacts, name='contacts'),
    url(r'^sitemap/$', views.sitemap, name='sitemap'),
    url(r'^support/twr/$', views.twr, name='twr'),
    url(r'^(?P<parent_alias>[\w-]+)/$', views.page, name='parent_page'),
    url(r'^(?P<parent_alias>[\w-]+)/(?P<child_alias>[\w-]+)/$', views.page, name='page'),
]

