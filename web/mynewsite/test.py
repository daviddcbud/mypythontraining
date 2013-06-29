#!/usr/bin/env python
from django.utils import timezone
from mytestapp.models import Book

b=Book(title='test',pub_date=timezone.now())
b.SaveMe()
print(Book.objects.all())
