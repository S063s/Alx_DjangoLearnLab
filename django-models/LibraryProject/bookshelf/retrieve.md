### Python Command
```python
>>> from bookshelf.models import Book
>>> retrieved_book = Book.objects.get(title="1984")
>>> print(f"Title: {retrieved_book.title}")
>>> print(f"Author: {retrieved_book.author}")
>>> print(f"Year: {retrieved_book.publication_year}")