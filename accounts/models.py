from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    user = models.ForeignKey(User, unique=True)
    avatar = models.ImageField(blank=True)
    website = models.URLField(max_length=200,blank=True)
    phone_number = models.CharField(max_length=200,blank=True)
    zip_code = models.CharField(max_length=200,blank=True)
    pv_api_token = models.CharField(max_length=200,blank=True)
    toggl_api_token = models.CharField(max_length=200,blank=True)
    hipchat_api_token = models.CharField(max_length=200,blank=True)
    
    def __unicode__(self):
        return u"%s" % (self.user)
    
    
