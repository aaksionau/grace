from django.db import models
from django.urls import reverse

EVENT_TYPES = {
    ('news','Новость'),
    ('future_events','Предстоящее событие'),
}
WEEKDAY_NAMES = [
    (0,'Понедельник'),
    (1,'Вторник'),
    (2,'Среда'),
    (3,'Четверг'),
    (4,'Пятница'),
    (5,'Суббота'),
    (6,'Воскресенье')
]
class Event(models.Model):
    title = models.CharField(max_length=255)
    date = models.DateField(auto_now=False)
    body = models.TextField(null=True, blank=True)
    short_description = models.TextField(null=True, blank=True)
    creation_date = models.DateTimeField(auto_now=True)
    published = models.BooleanField(default=False)
    event_type = models.CharField(max_length=20, choices=EVENT_TYPES, default='news')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        if self.event_type == "news":
            return reverse('news_item', args=[self.id])

        return reverse('event', args=[self.id])

    class Meta:
        verbose_name = 'событие'
        verbose_name_plural = 'события'

class ScheduleEvent(models.Model):
    title = models.CharField(max_length=255)
    time = models.TimeField(auto_now=False)
    event_day = models.IntegerField(choices=WEEKDAY_NAMES, default=6)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "регулярное событие"
        verbose_name_plural = "регулярные события"
