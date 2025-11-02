### Python Command
```python
>>> from bookshelf.models import Book
>>> book_instance = Book.objects.get(title="1984") 
>>> book_instance.title = "Nineteen Eighty-Four"
>>> book_instance.save()