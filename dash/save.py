from accounts.models import Profile 

def save_tokens(request):
    user = Profile.objects.get_or_create(user=request.user)[0]
    user.pv_api_token = request.POST['pv_api_token']
    user.hipchat_api_token = request.POST['hipchat_api_token']
    user.toggl_api_token = request.POST['toggl_api_token']
    user.save()

