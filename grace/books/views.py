from django.shortcuts import render
import csv
from django.views.decorators.cache import cache_page

from .models import *
from pages.models import Page


def library(request):
    page = Page.objects.get(alias='books')
    return render(request, 'books/index.html', {'data':page})

#Кэш на 60 дней
@cache_page(60 * 24 * 60 * 60)
def data(request):
    books = Book.objects.all()
    return render(request, 'books/data.html', {'books':books})


def book_import(request):
    with open('C:/projects/grace_church/grace/books/templates/books/catalog.csv', 'r', encoding='utf8') as csvfile:
        books_reader = csv.reader(csvfile)
        books = []
        for row in books_reader:
            book = Book()
            book.category = get_category(row[1])
            book.author = get_author(row[2])
            book.title = row[3]
            book.annotation = row[4]
            #book.save()
            books.append(book)
            

    return render(request, 'books/import.html', {'books':books})

def get_category(title):

    cleared_title = title.lower().replace('.', '').replace(' ', '')
    if cleared_title == 'дух':
        cleared_title = 'дин'
    if cleared_title == 'мирод':
        cleared_title = 'мир'
    
    category_db = Category.objects.filter(title=cleared_title).first()
    if category_db:
        return category_db
    else:
        category = Category()
        category.title = cleared_title
        category.save()
        return category

def get_author(name):
    if name == "?":
        name = "Неизвестный"
    author_db = Author.objects.filter(name=name).first()
    if author_db:
        return author_db
    else:
        author = Author()
        author.name = name
        author.save()
        return author