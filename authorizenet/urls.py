__author__ = 'KleinLieu'

from django.conf.urls.defaults import *
from authorizenet.views import process_payment_form
from django.views.generic.simple import direct_to_template

urlpatterns = patterns('',
    url(r'^order_success/$', direct_to_template, {'template': 'order_success.html'}),
    url(r'^$', process_payment_form),
)