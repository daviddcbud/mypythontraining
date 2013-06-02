from django.db import models

class Blog(models.Model):
    title= models.CharField(max_length=50)
    pub_date= models.DateTimeField('publish date')

    def __unicode__(self):
        return self.title


class Entry(models.Model):
    blog=models.ForeignKey(Blog)
    text=models.CharField(max_length=500)
    
    def __unicode(self):
        return self.text
