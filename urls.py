from django.conf.urls.defaults import patterns, include, url

from authorizetest import settings
from authorizenet.views import process_payment_form
from django.views.generic.simple import direct_to_template

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', include('authorizetest.authorizenet.urls')),
    # url(r'^authorizetest/', include('authorizetest.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    url(r'^site_media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    
    url(r'^authorize/', include('authorizetest.authorizenet.urls')),
    url(r'^order_success/$', direct_to_template, {'template': 'ordersuccess.html'}),
    url(r'^$', process_payment_form),
)
