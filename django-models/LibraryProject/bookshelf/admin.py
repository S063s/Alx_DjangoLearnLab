from django.contrib import admin
from .models import Book, Author, Genre

# Register your models here.

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # The fields below caused the error because 'publication_year' was removed.
    # We are using other fields that likely still exist.
    list_display = ('title', 'author', 'price') 
    list_filter = ('author',)
    list_editable = ('price',)
    search_fields = ('title', 'author__name')

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')
    search_fields = ('first_name', 'last_name')

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    pass
