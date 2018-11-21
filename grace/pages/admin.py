from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Page, Feedback, Settings

class PageAdmin(SummernoteModelAdmin):
    list_display = ('title', 'alias', 'parent', 'order', 'show_in_menu')
    fields = ('title','alias', 'parent', 'order', 'body','show_in_menu', 'seo_words','seo_description')

admin.site.register(Page, PageAdmin)
admin.site.register(Feedback)
admin.site.register(Settings)
