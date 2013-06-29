from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^blog/',include('blog.urls',namespace='blog')),
url(r'^site_media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': '/home/freeman/mypythontraining/web/testsite/media'}),

    # Examples:
    # url(r'^$', 'testsite.views.home', name='home'),
    # url(r'^testsite/', include('testsite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the min:
    # url(r'^admin/', include(admin.site.urls)),
)
