### Python Command
```python
>>> retrieved_book.publication_year = 2005
>>> retrieved_book.save()


>>> verified_book = Book.objects.get(title="1984")
>>> print(f"New Year: {verified_book.publication_year}")