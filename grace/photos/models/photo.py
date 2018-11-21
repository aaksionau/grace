from django.db import models
from .gallery import Gallery
from django.utils.safestring import mark_safe

class Photo(models.Model):
    description = models.CharField(max_length=1000, null=True, blank=True)
    image = models.FileField(upload_to='photos/%Y/%m',blank=False,null=False)
    thumbnail = models.FileField(upload_to='photos/%Y/%m/minified',blank=True,null=True)
    gallery = models.ForeignKey(
        'Gallery',
         on_delete=models.CASCADE
    )

    def image_tag(self):
        return mark_safe('<img src="/static/media/%s" width="150"/>' % (self.thumbnail))

    image_tag.short_description = 'Image'

    def __str__(self):
        return self.image.name

    class Meta:
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'