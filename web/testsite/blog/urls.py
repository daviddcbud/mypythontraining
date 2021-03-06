from django.conf.urls import patterns, include, url
from blog import views


# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover(

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),                   
    url(r'^(?P<id>\d+)/$', views.detail, name='detail'  ),
    url(r'^(?P<id>\d+)/update/$', views.update, name='update'  ),
    url(r'^about', views.About.as_view()),
url(r'^test', views.Test.as_view())
    # Examples:
    # url(r'^$', 'testsite.views.home', name='home'),
    # url(r'^testsite/', include('testsite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
