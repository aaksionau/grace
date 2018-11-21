from django.contrib import admin
from .models import *

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category')

admin.site.register(Category)
admin.site.register(Author)
admin.site.register(Book, BookAdmin)

