from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Tag, Biblebook, Sermon, Preacher

class SermonAdmin(SummernoteModelAdmin):
    list_display = ('title', 'bible_book', 'chapter_and_verses', 'preacher')

class MinistryAdmin(SummernoteModelAdmin):
    list_display = ('title','alias','order','responsible_person')
    fields = ('title','alias','short_description','order', 'body', 'main_image','responsible_person', 'person_email', 'seo_words','seo_description')

admin.site.register(Sermon, SermonAdmin)

admin.site.register(Tag)
admin.site.register(Biblebook)
admin.site.register(Preacher)
