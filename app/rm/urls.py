from django.conf.urls.defaults import patterns, include, url
from django.conf.urls.defaults import *

urlpatterns = patterns('rm.views',
    url(r'^$', 'index', name='index'),
    #url(r'^profile/contact/add.json', 'add_contact', name='add_contact'),
    url(r'^accounts/profile/', 'account', name='account'),
    url(r'^logout/$', 'user_logout', name='user_logout'),
    url(r'^login-error/$', 'login_error', name='login_error'),
)

