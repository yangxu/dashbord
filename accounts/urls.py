from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'dash.views.index', name='index'),
    url(r'login/', 'accounts.views.login', name='login'),
    url(r'register/', 'accounts.views.register', name='register'),
    url(r'logout/', 'accounts.views.logout', name='logout'),
    url(r'profile/', 'accounts.views.profile', name='profile'),
    url(r'settings/', 'accounts.views.settings', name='settings'),
)

