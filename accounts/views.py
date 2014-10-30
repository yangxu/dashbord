from django.shortcuts import render
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template import RequestContext
from django.contrib.auth import authenticate, login as dj_login, logout as dj_logout
from django.contrib.auth.decorators import login_required
from accounts.models import Profile

def login(request):
    if request.method == 'GET':
       return render_to_response('dash/pages/page_login.html', {}, context_instance=RequestContext(request))
    elif request.method == 'POST':
        username = request.POST['username']
        print username
        password = request.POST['password']
        print password
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                dj_login(request, user)
                print request.META['HTTP_REFERER']
                return redirect("/") # Redirect to a success page.
            else: # Return a 'disabled account' error message
                return render_to_response('dash/pages/page_login.html', {'message': "disabled account"}, context_instance=RequestContext(request))
        else: # Return an 'invalid login' error message.
            return render_to_response('dash/pages/page_login.html', {'message': 'invalid login'}, context_instance=RequestContext(request))

def logout(request):
    dj_logout(request)
    return render_to_response('dash/pages/page_login.html', {}, context_instance=RequestContext(request))

def register(request):
    #return None
    return render_to_response('dash/pages/page_register.html', {}, context_instance=RequestContext(request))

@login_required
def profile(request):
    return render_to_response('accounts/profile.html', {}, context_instance=RequestContext(request))

@login_required
def settings(request):
    user = Profile.objects.get(user = request.user)
    return render_to_response('accounts/settings.html', {'user':user}, context_instance=RequestContext(request))
    


