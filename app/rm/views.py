from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.auth import logout, login, authenticate
from django.utils import simplejson
from django.contrib.messages.api import get_messages    
from django.core.context_processors import csrf
from social_auth.models import *

import requests
import simplejson as json

PROVIDERS=['facebook', 'twitter', 'google', 'linkedin']

def index(request):
    c = RequestContext(request, {})
    return render_to_response('base.html', c)
    
def account(request):
    social_accounts = UserSocialAuth.objects.filter(user=request.user)
    accounts=[]
    for provider in PROVIDERS:
        found = False
        for account in social_accounts:
            if account.provider == provider:
                found = True            
        accounts.append({'provider': provider, 'active': found})
        
    c = RequestContext(request, {
        'accounts': accounts,
    })
    return render_to_response('account/profile.html', c)
    
    
def login_error(request):
    c = RequestContext(request, {})
    for msg in get_messages(request):
        print msg.message
    return render_to_response('error.html',c)

def user_logout(request):
    logout(request)
    c = RequestContext(request, {})
    return render_to_response('base.html', c)