from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'категории'
        verbose_name_plural = 'категория'

class Author(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'автор'
        verbose_name_plural = 'авторы'

class Book(models.Model):
    title = models.CharField(max_length=500)
    author = models.ForeignKey(
        Author,
        on_delete=models.DO_NOTHING
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.DO_NOTHING
    )
    annotation = models.CharField(max_length=1000)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'книга'
        verbose_name_plural = 'книги'

