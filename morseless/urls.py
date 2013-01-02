from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    #
    # url(r'^morseless/', include('morseless.foo.urls')),
    url(r'^$', 'morsecodec.views.home', name='home'),
    url(r'^decode$', 'morsecodec.views.decode', name='decode'),

    url(r'logs/(?P<log_name>[\w-]+)$', 'log4javascript.views.log', name='log'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
