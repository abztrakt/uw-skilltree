from django.conf import settings
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login, logout
from django.core.context_processors import csrf
from skilltreeapp.forms import LoginForm
from django.shortcuts import render_to_response, HttpResponseRedirect

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

def tools_login(request):
    """ Login a user. Called by @login_required decorator.
    """
    c = {}
    c.update(csrf(request))
    if request.user.is_authenticated():
        try:
            return HttpResponseRedirect(request.GET['next'])
        except:
            return HttpResponseRedirect('/')
    elif request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/')
                else:
                    return HttpResponseRedirect('/')
    else:
        form = LoginForm()

    return render_to_response('pages/login.html', locals(), context_instance=RequestContext(request))

def tools_logout(request):
    """ Manually log a user out.
    """
    logout(request)
    return HttpResponseRedirect('/')
