from django.db import models

PARTS_OF_BIBLE = {
    ('ot','Ветхий Завет'),
    ('nt','Новый Завет'),
}

class Biblebook(models.Model):
    title = models.CharField(max_length=255)
    abbreviation = models.CharField(max_length=70, blank=True, null=True)
    order = models.IntegerField()
    part_of_bible = models.CharField(max_length=2, choices=PARTS_OF_BIBLE, default='nt')
    image = models.FileField(upload_to='bible',blank=True,null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'книга Библии'
        verbose_name_plural = 'книги Библии'