from django.db import models

class Preacher(models.Model):
    name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255, unique=True)
    description = models.TextField(null=True, blank=True)
    is_member = models.BooleanField()
    photo = models.FileField(upload_to='preachers')

    def __str__(self):
        return self.last_name + ' ' + self.name

    class Meta:
        verbose_name = 'проповедник'
        verbose_name_plural = 'проповедники'