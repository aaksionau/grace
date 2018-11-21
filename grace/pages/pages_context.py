from django.contrib.sites.models import Site
from django.db.models import Prefetch, Count
from datetime import date

from .models import Page
from sermons.models import Biblebook
from events.models import Event

def show_pages_menu(request):
    pages_menu = Page.objects.filter(show_in_menu=True, parent=None).order_by(
        'order').prefetch_related(
                Prefetch(
                    "children",
                    queryset=Page.objects.filter(show_in_menu=True),
                    to_attr=None
                )
        )

    parent_alias_active, _, child_alias_active = request.get_full_path().strip('/').partition('/')

    aside_menu_items = Page.objects.filter(parent__alias=parent_alias_active, show_in_menu=True).order_by('order')

    sermon_books = Biblebook.objects.annotate(num_sermons = Count('sermon')).order_by('-num_sermons')[:5]

    events = Event.objects.filter(date__gte=date.today(), published=True, event_type='future_events').order_by('-date')[:3]

    return {'pages_menu': pages_menu,
            'aside_menu_items': aside_menu_items,
            'sermon_books': sermon_books,
            'aside_events':events,
            'active_parent_alias': parent_alias_active,
            'active_child_alias': child_alias_active}


def base_url(request):
    return {
        'BASE_URL': 'http://{0}'.format(Site.objects.get_current().domain)
    }

