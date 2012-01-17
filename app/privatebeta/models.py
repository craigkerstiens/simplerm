import datetime
from django.db import models
from django.utils.translation import ugettext_lazy as _

class InviteRequest(models.Model):
    email = models.EmailField(unique=True)
    first_name = models.CharField(_('First Name'), max_length=50)
    last_name = models.CharField(_('Last Name'), max_length=50)
    created = models.DateTimeField(_('Created'), default=datetime.datetime.now)
    invited = models.BooleanField(_('Invited'), default=False)

    def __unicode__(self):
        return _('Invite for %(email)s') % {'email': self.email}
