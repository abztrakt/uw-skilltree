from django.conf import settings
from django.template import RequestContext
from django.shortcuts import render_to_response

# Create your views here.
                        
def home(request):
    params = {}
    return render_to_response('pages/home.html', params, context_instance=RequestContext(request))

def basic(request):
    params = {}
    return render_to_response('pages/basic.html', params, context_instance=RequestContext(request))

def hybrid(request):
    params = {}
    return render_to_response('pages/hybrid.html', params, context_instance=RequestContext(request))
