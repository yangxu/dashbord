from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'dash.views.index', name='index'),
    url(r'^pv_json/', 'dash.views.pv_json', name='pv_json'),
    url(r'^pivotal/project/(?P<project_id>[-\w]+)','dash.views.project', name='project_id'),
    #url(r'^accounts/login/', 'dash.views.login', name='login'),
    #url(r'^register/', 'dash.views.register', name='login'),
)

