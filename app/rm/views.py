from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.auth import logout, login, authenticate
from django.utils import simplejson
from django.contrib.messages.api import get_messages    
from django.core.context_processors import csrf

import requests
import simplejson as json

def index(request):
    c = RequestContext(request, {})
    return render_to_response('base.html', c)
    
def login_error(request):
    c = RequestContext(request, {})
    print request
    for msg in get_messages(request):
        print msg.message
    return render_to_response('error.html',c)

def user_logout(request):
    logout(request)
    c = RequestContext(request, {})
    return render_to_response('base.html', c)