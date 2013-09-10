from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from forms import AddMediaForm
from django.forms import ModelForm
from models import Media
from User.Account.models import Disk


def addmedia(request, disk_id):
    if request.method == 'POST':
        thedisk = Disk.objects.get(pk=disk_id)
        if request.FILES: #should make this if form.cleaned_data['category'] != 'Text':
            form = AddMediaForm(request.POST, request.FILES)
        
            if form.is_valid():
                new_media = Media.objects.create(name=form.cleaned_data['name'],
                                            docfile = request.FILES['docfile'],
                                            description_body = form.cleaned_data['description_body'],
                                            description_excerpt = form.cleaned_data['description_excerpt'],
                                            user = request.user,
                                            disk = thedisk,
                                            size = request.FILES['docfile'].size,
                                            category = form.cleaned_data['category'],
                                            group = form.cleaned_data['group'],
                                            enable_comments = form.cleaned_data['enable_comments'],
                                            public = form.cleaned_data['public'])
                thedisk.space_used += new_media.size
                thedisk.space_left -= new_media.size
                thedisk.save()
                return HttpResponseRedirect(new_media.get_absolute_url())
                                            
        else:
            form = AddMediaForm(request.POST)
        
            if form.is_valid():
                new_media = Media.objects.create(name=form.cleaned_data['name'],
                                                description_body = form.cleaned_data['description_body'],
                                                description_excerpt = form.cleaned_data['description_excerpt'],
                                                user = request.user,
                                                disk = thedisk,
                                                category = form.cleaned_data['category'],
                                                group = form.cleaned_data['group'],
                                                enable_comments = form.cleaned_data['enable_comments'],
                                                public = form.cleaned_data['public'])
                                            
                return HttpResponseRedirect(new_media.get_absolute_url())
        
            
    else:
        form = AddMediaForm(request.POST, request.FILES)
        
    return render_to_response('Media/add_media_form.html',
                                { 'form': form,
                                'disk_id':disk_id},
                                RequestContext(request, {}))

from django.core.urlresolvers import reverse
                                
def deletemedia(request, media_id):
    media = Media.objects.get(pk=media_id)
    thesize = media.size
    media_group = media.group
    media_disk = media.disk
    if media_group == None:
        url = '/u/%s/database/%s/' %(request.user.username, media_disk.letter)
    else:
        url = media_group.get_absolute_url()
    media.delete()
    media_disk.space_used -= thesize
    media_disk.space_left += thesize
    media_disk.save()
    return HttpResponseRedirect(url)
    
    
    
    
    
    

