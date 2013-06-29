from django.shortcuts import render,get_object_or_404
from blog.models import Entry,Blog
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views.generic.base import View

def index(request):
    list=Entry.objects.all()
    
    return render(request,'blog/index.html',{'data':list})

def detail(request, id):
    entry=get_object_or_404(Entry,pk=id)
    return render(request, 'blog/detail.html', {'data':entry})

def update(request,id):
    entry=get_object_or_404(Entry,pk=id)
    entry.text=request.POST['text']
    entry.save()
    return HttpResponseRedirect(reverse('blog:index' ))
    

class About(View):
    def get(self,request):
        return render(request,'blog/about.html',{'message':'hello bob'})

    
class Test(View):
    def get(self,request):
        return render(request,'blog/test.html',{'message':'hello bob'})

    
