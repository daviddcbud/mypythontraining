from django.conf.urls import patterns, include, url

from mytestapp import views

urlpatterns=patterns('',
   url(r'^$', views.index, name='index'),
   
url(r'^test/getnames', views.getnames, name='getnames'),
url(r'^test/', views.test, name='test')

)
