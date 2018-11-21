from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from .models import Event, ScheduleEvent

# Register your models here.

class EventAdmin(SummernoteModelAdmin):
    list_display = ('title', 'date', 'body', 'event_type', 'published')

admin.site.register(Event, EventAdmin)
admin.site.register(ScheduleEvent)