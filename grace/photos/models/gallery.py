from django.db import models
from django.urls import reverse

from pages.models import Seo

class Gallery(Seo):
    title = models.CharField(max_length=255)
    alias = models.CharField(max_length=255, unique=True)
    body = models.TextField(null=True, blank=True)
    main_image = models.FileField(upload_to='galleries/%Y/%m')
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('gallery', args=[self.alias])

    class Meta:
        verbose_name = 'Фотогалерея'
        verbose_name_plural = 'Фотогалереи'