from django.shortcuts import render,get_object_or_404
from blog.models import Entry,Blog
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

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
    
