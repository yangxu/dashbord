from django.db import models

# Create your models here.
from django.db import models

class Row(models.Model):
    fileid = models.CharField(max_length=6,db_index=True)
    filetype = models.CharField(max_length=6,blank=True,null=True,db_index=True)
    name = models.CharField(max_length=100, blank=True)
