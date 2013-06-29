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

class Person(models.Model):
    last_name=models.CharField('Last Name',max_length=50)
    first_name=models.CharField('First Name',max_length=50)
    address=models.CharField('Address',max_length=500)

    def __unicode__(self):
        return self.last_name + ',' + self.first_name


class Skill(models.Model):
    description=models.CharField('Description',max_length=50)
    people=models.ManyToManyField(Person,through='SkillToPerson')


class SkillToPerson(models.Model):
    person=models.ForeignKey(Person)
    skill=models.ForeignKey(Skill)
    level=models.IntegerField()
    
