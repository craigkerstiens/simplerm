from django.core.management.base import BaseCommand, CommandError
from app.rm.utils import *
from social_auth.models import *

class Command(BaseCommand):
    args = '<social_auth_id social_auth_id ...>'
    help = 'Loads fb messages for a given user'
        
    def handle(self, *args, **options):
        for user in UserSocialAuth.objects.all():
            try:
                facebook_messages(user)
            except:
                raise CommandError('User "%s" does not exist' % user.id)
                
            