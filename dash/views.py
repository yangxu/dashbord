from django.shortcuts import render
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template import RequestContext
from django.contrib.auth import authenticate, login as dj_login, logout as dj_logout
from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponse
from dash import save
from accounts.models import Profile
import json
from busyflow.pivotal import PivotalClient

@login_required
def index(request):
    #return None
    if request.method == 'POST':
       if 'hipchat_api_token' in request.POST and 'pv_api_token' in request.POST and 'toggl_api_token' in request.POST:
          save.save_tokens(request)
       return render_to_response('dash/index.html', {}, context_instance=RequestContext(request))
    elif request.method == 'GET':
       if request.user.is_authenticated():
          user, create = Profile.objects.get_or_create(user = request.user)
          if create:
             projects = []
          else:
             client = PivotalClient(token=user.pv_api_token, cache='pvcache')
             projects = client.projects.all()['projects']

          return render_to_response('dash/index.html', {'projects':projects}, context_instance=RequestContext(request))
       else:
          return redirect("/login")

def project(request, project_id):
    return render_to_response('accounts/project.html', {"project_id":project_id}, context_instance=RequestContext(request))

def default(obj):
    """Default JSON serializer."""
    import calendar, datetime

    if isinstance(obj, datetime.datetime):
        if obj.utcoffset() is not None:
            obj = obj - obj.utcoffset()
    millis = int( 
        calendar.timegm(obj.timetuple()) * 1000 + 
        obj.microsecond / 1000
    )
    return millis



@login_required
def pv_json(request):
    #http://localhost:8000/pv_json/?project=442737 
    #try:
       user = Profile.objects.get(user = request.user)
       client = PivotalClient(token=user.pv_api_token, cache='pvcache')
       projects = client.projects.all()['projects']
       if "project" in request.GET:
          prj = int(request.GET["project"])
          if request.GET["target"]=="current":
             iterations = client.iterations.current(prj)
          elif request.GET["target"]=="backlog":
             iterations = client.iterations.backlog(prj)
          elif request.GET["target"]=="done":
             iterations = client.iterations.done(prj)

          return HttpResponse(json.dumps(iterations, default=default), content_type="application/json")

       iterations = client.iterations.current(projects[0]['id'])
       return HttpResponse(json.dumps(projects, default=default), content_type="application/json")
    #except:
    #   return HttpResponse(json.dumps({'Result':'Please setup you tokens in your setting'}), content_type="application/json") 



