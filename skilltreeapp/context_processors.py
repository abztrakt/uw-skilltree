""" context_processors.py

To make this available in your RequestContext() add
skilltreeapp.context_processors.is_desktop to your
TEMPLATE_CONTEXT_PROCESSORS setting.
"""
from django.conf import settings

def is_desktop(request):
    """ See if the browser is desktop
    """
    if request.MOBILE == 0:
        return {'is_desktop' : True}
    else:
        return {'is_desktop' : False}
