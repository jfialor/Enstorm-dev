from django.db import models
from django.contrib.auth.models import User
from Media.models import Media, Type

# Create your models here.


class ShelfType(models.Model):
    name = models.CharField(max_length=30)
    mediatype = models.ForeignKey(Type)
    
    def __unicode__(self):
        return self.name
    

class Shelf(models.Model):
    name = models.CharField(max_length=30)
    user = models.ForeignKey(User)
    media = models.ManyToManyField(Media)
    shelf_type = models.ForeignKey(ShelfType)
    
    
    #several other shelf fields. have to add the same for media
    description = models.TextField(blank=True)
    inspiration = models.TextField(blank=True)
    
    
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    
    def __unicode__(self):
        return self.name
        
    def get_absolute_url(self):
        return ('user_library_shelf', (), {'username': self.user.username, 'shelf_id': self.id})
    get_absolute_url = models.permalink(get_absolute_url)
    
        
        
    
