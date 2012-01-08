import django.dispatch

contact_update = django.dispatch.Signal(providing_args=["post","request"])