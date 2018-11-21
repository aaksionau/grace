from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Photo, Gallery

class GalleryAdmin(SummernoteModelAdmin):
    list_display = ('title', 'alias')
    fields = ('title','alias','body','main_image', 'seo_words','seo_description')

admin.site.register(Gallery, GalleryAdmin)

class PhotoAdmin(admin.ModelAdmin):
    list_display = ('image_tag', 'description', 'gallery')
    fields = ( 'image', 'thumbnail', 'description','gallery')
    readonly_fields = ('image_tag',)

admin.site.register(Photo, PhotoAdmin)
