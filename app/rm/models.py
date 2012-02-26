from django.db import models
from django.contrib.auth.models import User
import gmail

MEDIUM_CHOICES = (
    (1, u'Email'),
    (2, u'Text'),
    (3, u'IM'),
    (4, u'Phone'),
    (5, u'Facebook'),
    (6, u'In Person'))

# Generic Models
class Service(models.Model):
	name = models.CharField(max_length=200)
	medium = models.IntegerField(choices=MEDIUM_CHOICES, blank=True, null=True)

	def __unicode__(self):
		return self.name

# Users contacts models

class Contact(models.Model):
    user = models.ForeignKey(User, blank=True, null=True)
    name = models.CharField(max_length=200)
    def __unicode__(self):
        return self.name

class ContactAccount(models.Model):
    user = models.ForeignKey(User, blank=True, null=True)
    contact = models.ForeignKey(Contact, blank=True, null=True)
    service = models.IntegerField(choices=MEDIUM_CHOICES, blank=True, null=True)
    description = models.TextField(blank=True,null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    account_id = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name


# Items connecting users and their contacts

class Interaction(models.Model):
    source = models.ForeignKey(ContactAccount,related_name="%(app_label)s_%(class)s_source")
    destination = models.ManyToManyField(ContactAccount,related_name="%(app_label)s_%(class)s_dest")
    content = models.TextField(blank=True,null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    message_id = models.CharField(null=True, blank=True,max_length=30)
    def __unicode__(self):
        return self.thread

class Relationship(models.Model):
	interactions = models.ManyToManyField(Interaction, blank=True, null=True)
	relationship_type = models.CharField(max_length=50)
	user = models.ForeignKey(User)

	def __unicode__(self):
		return self.relationship_type
		
class UserProfile(models.Model):
    user = models.OneToOneField(User)
    phone_no = models.CharField(max_length=50)
    email = models.BooleanField(default=False)
    phone = models.BooleanField(default=False)
    
		
from social_auth.signals import pre_update
from social_auth.backends.google import GoogleOAuth2Backend

def google_extra_values(sender, user, response, details, **kwargs):
    #print sender
    #print user
    gmail.get_messages('imap.googlemail.com', response['id_token'])
    #print details
    return True
    
from social_auth.signals import pre_update
from social_auth.backends.facebook import FacebookBackend

def facebook_extra_values(sender, user, response, details, **kwargs):
    obj, created = ContactAccount.objects.get_or_create(service=5, user=user, account_id=response.get('id'))
    if created:
        obj.save()
    return True

pre_update.connect(facebook_extra_values, sender=FacebookBackend)
pre_update.connect(google_extra_values, sender=GoogleOAuth2Backend)
