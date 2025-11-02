### Python Command
```python
>>> verified_book.delete()

>>> try:
...     Book.objects.get(title="1984")
... except Book.DoesNotExist:
...     print("Book successfully deleted.")