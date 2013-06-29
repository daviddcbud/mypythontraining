#!/usr/bin/env python
from django.db import models
from MyBase import BaseDBClass

class Book(BaseDBClass):
    title= models.CharField(max_length=50)
    pub_date= models.DateTimeField('publish date')

    def __unicode__(self):
        return self.title

