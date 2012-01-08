from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User


from rm.models import *

admin.site.register(Service)
admin.site.register(Contact)
admin.site.register(ContactAccount)
admin.site.register(Interaction)
admin.site.register(Relationship)
