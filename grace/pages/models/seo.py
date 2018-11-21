from django.db import models

class Seo(models.Model):
    seo_words = models.CharField(max_length=255, null=True, blank=True)
    seo_description = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        abstract = True
