import datetime
from django.db import models
from django.contrib.auth.models import User
from User.Account.models import Disk

class Group(models.Model):
    user = models.ForeignKey(User)
    name = models.CharField(max_length=250)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    description = models.TextField(blank=True)
    disk = models.ForeignKey(Disk)
    
    
    description_html = models.TextField(blank=True)
    
    def __unicode__(self):
        return self.name
        
    def get_absolute_url(self):
        return ('user_creation_groups', (), {'username':self.user.username,'group_id': self.id})
    get_absolute_url = models.permalink(get_absolute_url) 
    
    
    def media_list(self):
        return self.media_set.all()
        
    def save(self, force_insert=False, force_update=False, *args, **kwargs):
        #stuff about description html
        super(Group, self).save(force_insert, force_update)
        
    class Meta: 
         app_label = 'Creations'