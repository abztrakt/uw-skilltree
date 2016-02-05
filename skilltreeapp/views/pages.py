from django.conf import settings
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login, logout
from django.core.context_processors import csrf
from skilltreeapp.forms import LoginForm
from django.shortcuts import render_to_response, HttpResponseRedirect
import datetime
from labgeeks_hermes.models import Notification
from labgeeks_hermes.forms import NotificationForm

# Create your views here.

def home(request):
    params = {}
    c = {}
    c.update(csrf(request))
    if request.user.is_authenticated():
        # hermes code goes here
        locations = request.user.location_set.all()

        now = datetime.datetime.now()

        notifications = Notification.objects.all()
        events = []
        alerts = []
        for noti in notifications:
            if noti.due_date:
                if now.date() - noti.due_date.date() >= datetime.timedelta(days=1):
                    noti.archived = True
                elif not noti.due_date.date() - now.date() > datetime.timedelta(days=7) and not noti.archived:
                    events.append(noti)
            else:
                if not noti.archived:
                    alerts.append(noti)
        events.sort(key=lambda x: x.due_date)

        form_is_valid = True
        if request.method == 'POST':
            archive_ids = request.POST.getlist('pk')
            if archive_ids:
                for archive_id in archive_ids:
                    notif = Notification.objects.get(pk=archive_id)
                    notif.archived = True
                    notif.save()
                return HttpResponseRedirect('/')

            form = NotificationForm(request.POST)
            if form.is_valid():
                form_is_valid = True
                notification = form.save(commit=False)
                notification.user = request.user
                if notification.due_date:
                    if now.date() - notification.due_date.date() >= datetime.timedelta(days=1):
                        notification.archived = True
                notification.save()
                return HttpResponseRedirect('/')
            else:
                form_is_valid = False
        else:
            form = NotificationForm()

        params = {
            'request': request,
            'events': events,
            'alerts': alerts,
            'form': form,
            'c': c,
        }

        return render_to_response('pages/home.html', params, context_instance=RequestContext(request))
    else:
        form = LoginForm()
        params = { 'form': form }
        return HttpResponseRedirect('/accounts/login')

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
