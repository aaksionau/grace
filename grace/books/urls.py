from django.conf.urls import url, include
from . import views

urlpatterns = [
    #url(r'^import/$', views.book_import, name='book_import')
    url(r'^$', views.library, name='library'),
    url(r'^data/$', views.data, name='books_data')
]