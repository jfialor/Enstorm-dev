import datetime
from django.db import models
from django.contrib.auth.models import User
from User.Creations.creationgroups.Media import Group
from User.Account.models import Disk
from markdown import markdown

class Type(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(unique=True) #shall be populated with name
    description = models.TextField()
    
    def __unicode__(self):
        return self.name
        
    class Meta:
        ordering=('name',)
        verbose_name_plural = 'Media Categories'
        
    def public_media_set(self):
        from Media.models import Media
        return self.media_set.filter(public=True)
        
class SubCategory(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    
    def __unicode__(self):
        return self.name
        
    def public_media_set(self):
        from Media.models import Media
        return self.media_set.filter(public=True) 
        
        
def content_file_name(instance, filename):
    return '/'.join(['UploadedMedia', instance.user.username, filename])
        

class Media(models.Model):
    name = models.CharField(max_length=250)
    description_body = models.TextField(blank=True)
    description_excerpt = models.TextField(blank=True)
    category = models.ForeignKey(Type, related_name='media')
    size = models.BigIntegerField()
    
    user = models.ForeignKey(User)
    disk = models.ForeignKey(Disk)
    group = models.ForeignKey(Group, blank=True, null=True)
    
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    
    enable_comments = models.BooleanField(default=True)
    
    
    #no need fo these two with tinymce setup
    description_full_html = models.TextField(blank=True, editable=False)
    description_excerpt_html = models.TextField(blank=True, editable=False)
    
    public = models.BooleanField(default=True)
    
    docfile = models.FileField(upload_to=content_file_name,max_length = 1000,blank = True)
    
    def __unicode__(self):
        return self.name
    
    def get_absolute_url(self):
        return ('media_detail', (), {'pk': self.id})
    get_absolute_url = models.permalink(get_absolute_url)
    
    class Meta:
        app_label = 'Media'
        ordering =  ('date_updated',)
        verbose_name_plural = 'Media'
        
    def save(self, force_insert=False, force_update=False,*args, **kwargs):
            self.description_full_html = markdown(self.description_body)
            self.description_excerpt_html = markdown(self.description_excerpt)
            super(Media, self).save(force_insert, force_update)
            

        
        
        
        
        
        
        
        
        
        
        
        
        
        
    
