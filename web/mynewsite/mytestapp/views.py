# Create your views here.
from django.shortcuts import render, get_object_or_404
from mytestapp.models import Book
from django.utils import simplejson
from django.http import HttpResponse
from django.utils import timezone
from datetime import datetime
def index(request):
    mydata={'books':Book.objects.all(), 'value':'www.microsoft.com'}
    return render(request,'mytestapp/index.html',mydata)

def test(request):
	mydata={'value':'check out\n www.microsoft.com','value2':'1', 'startdate':datetime.strptime('2013 06 28 09:00:00', '%Y %m %d %H:%M:%S'), 'from_date':timezone.now()}
	return render(request,'mytestapp/test.html',mydata)

def getnames(request):
	b=Book()
	b.title='dave'
	b.pub_date=timezone.now()
	b.modified_date=timezone.now()
	b.created_date=timezone.now()
	#b.save()
	mydata=Book.objects.all()
	jsondata=[]
	for x in mydata:
		jsondata.append({'title':x.title, 'id': x.id})
	
	return HttpResponse(simplejson.dumps(jsondata))
