from django.db import models
from django.core.validators import RegexValidator
from django.urls import reverse


from .biblebook import Biblebook
from .preacher import Preacher
from .tag import Tag


class Sermon(models.Model):
    title = models.CharField(max_length=255, blank=False, null=False)
    bible_book = models.ForeignKey(
        Biblebook,
        on_delete=models.DO_NOTHING
    )
    chapter_and_verses = models.CharField(
        max_length=20,
        blank=False,
        null=False,
        validators=[
            RegexValidator(
                regex='^\d{1,3}:\d{1,3}-{0,1}\d{0,3}$',
                message='Место Писания должно быть в формате: 1:1, 1:10-21',
                code='invalid_chapter_and_verses'
            )
        ]
    )
    date = models.DateTimeField(auto_now=False)
    audio = models.FileField(upload_to="sermons/")
    topics = models.ManyToManyField(Tag)
    preacher = models.ForeignKey(
        Preacher,
        on_delete=models.DO_NOTHING
    )
    description = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse("sermon", args=[self.id])

    def __str__(self):
        return self.title + ' (' + self.bible_book.title + ' ' + self.chapter_and_verses + ')'

    class Meta:
        verbose_name = 'проповедь'
        verbose_name_plural = 'проповеди'
