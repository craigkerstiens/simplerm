from social_auth.models import *
from app.rm.models import *
from datetime import datetime
import dateutil.parser
import simplejson as json
import sys
import requests
import urllib2

def facebook_messages(user):
    FB_URL = 'https://graph.facebook.com/%s'
    url = FB_URL % ('me/inbox?access_token=%s&limit=1&offset=0' % user.extra_data['access_token'])
    data = {
        'access_token': user.extra_data['access_token'],
        'limit': 1,
        'offset': 1
    }
    response = requests.get(url, data=data)
    message_list = json.loads(response.content)
    ca = ContactAccount.objects.filter(contact__in=(Contact.objects.filter(user=user.user)))
    ca_list = []
    for contact in ca:
        ca_list.append(contact.account_id)
    messages = []
    
    current_user = ContactAccount.objects.get(service=5, user=user.user)
    for messages in message_list['data']:
        try:
            # Get the other users in the thread
            if messages.get('from').get('id') == ContactAccount.objects.get(service=5, user=user.user).id:
                other_user = messages.get('from')
            else:
                other_user = messages.get('to')
            
            # Create a contact account
            for user_list in other_user.get('data'):
                contact_account, created = ContactAccount.objects.get_or_create(service=5, account_id=user_list['id'])
                if created:
                    contact = Contact(user=user.user, name=user_list['name'])
                    contact.save()
                    
            # Load all messages
            # STILL NEED TO CLEANUP SOURCES
            for message in messages['comments']['data']:
                if message['from']['id'] == current_user.account_id:
                    source = current_user
                    destination = contact_account
                else:
                    source = contact_account
                    destination = current_user
                dt=datetime.strptime(message['created_time'], '%Y-%m-%dT%H:%M:%S+%f')
                interaction, created = Interaction.objects.get_or_create(source=source, content=message['message'], created_at=dt, message_id=message['id'])
                # NEED TO ADD DESTINATION
        except:
            print "Unexpected error:", sys.exc_info()
    return message_list
    
def facebook_user(request, user):
    fb_user = UserSocialAuth.objects.get(user=request.user, provider='facebook')
    FB_URL = 'https://graph.facebook.com/%s'
    url = FB_URL % ('%s?access_token=%s' % (user, fb_user.extra_data['access_token']))
    user = json.loads(urllib2.urlopen(url).read())
    return user['name']