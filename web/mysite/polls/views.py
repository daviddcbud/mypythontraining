from django.shortcuts import render

from polls.models import Poll

def index(request):
    polls=Poll.objects.all()
    context={'polls': polls,'error_message':'test'}
    return render(request,'polls/index.html',context)

def detail(request):
    pass
