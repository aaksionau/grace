from django.db import models
from django.urls import reverse
from .seo import Seo
from django.contrib import admin


class Page(Seo):
    alias = models.SlugField(unique=True)
    title = models.CharField(max_length=255)
    body = models.TextField(null=True, blank=True)
    parent = models.ForeignKey(
        'self', 
        blank=True, 
        null=True, 
        related_name='children',
        on_delete=models.DO_NOTHING)

    order = models.PositiveSmallIntegerField(default=0)
    show_in_menu = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('page', args=[self.parent.alias, self.alias])

    class Meta:
        verbose_name = 'Страница сайта'
        verbose_name_plural = 'Страницы сайта'
