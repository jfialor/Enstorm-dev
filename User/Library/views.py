from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponseRedirect
from User.Library.models import Shelf
from forms import AddShelfForm
from django.template import RequestContext
#from User.Creations.creationgroups.Media import Group
from Media.models import Media
#from django.views.generic.list import ListView

from django import forms

from forms import AddMediaForm
from django.forms import ModelForm
from User.Account.models import Disk



def library_home(request, username):
    #if request.user.username != username:
        #if request.user.is_authenticated:
    
    #if request.user.username is username:
    User = request.user
    form = AddShelfForm(user=request.user)
    user_library = {'user': User,
                    'user_shelfs': User.shelf_set.all(),
                    'form':form}
                    
    return render_to_response('Library/home.html', user_library, RequestContext(request, {}))
    
def library_shelf(request, username, shelf_id):
    #if request.user.username != username:
        #if request.user.is_authenticated:
    
    #if request.user.username is username:
    User = request.user
    form = AddShelfForm(user=request.user)
    shelf = Shelf.objects.get(pk=shelf_id)
    user_library = {'user': User,
                    'user_shelfs': User.shelf_set.all(),
                    'form':form,
                    'theshelf':shelf}
                    
    return render_to_response('Library/home.html', user_library, RequestContext(request, {}))    
    
    
    
def add_shelf(request, username):
    user = request.user
    if request.method == 'POST':
        form = AddShelfForm(user=request.user, data=request.POST)
        #form = PamphletForm(data=request.POST)
        if form.is_valid():
            new_shelf = form.save()#.save(commit=False)
            #new_pamphlet.artist = request.user
            return HttpResponseRedirect(new_shelf.get_absolute_url())
        
    else:
        form = AddShelfForm(user=request.user)
    
    return HttpResponseRedirect('/u/%s/library/' % (user.username))
    
def internewshelf(request, username):
    User = request.user
    form = AddShelfForm(user=request.user)
    user_library = {'user': User,
                    'user_shelfs': User.shelf_set.all(),
                    'form':form}
    return render_to_response('Library/internewshelf.html', user_library, RequestContext(request, {}))
        
    
def intershelve(request, username, media_id):
    user = request.user
    return render_to_response('Library/intershelve.html',{'user': user, 'user_shelfs':user.shelf_set.all(), 'media_id':media_id})
    
def shelve(request, username, media_id, shelf_id):
    user = request.user
    media = Media.objects.get(pk=media_id)
    shelf = Shelf.objects.get(pk=shelf_id)
    shelf.media.add(media)
    shelf.save()
    return HttpResponseRedirect('/u/%s/library/' % (user.username))
    
    
    
def mediaview(request, username, shelf_id, media_id):
    #if request.user.username != username:
        #if request.user.is_authenticated:
    
    #if request.user.username is username:
    User = request.user
    form = AddShelfForm(user=request.user)
    shelf = Shelf.objects.get(pk=shelf_id)
    media = Media.objects.get(pk=media_id)
    user_library = {'user': User,
                    'user_shelfs': User.shelf_set.all(),
                    'form':form,
                    'theshelf':shelf,
                    'media':media}
                    
    return render_to_response('Library/mediaview.html', user_library, RequestContext(request, {}))
    

    
def newmedia(request, username, shelf_id):
    shelf = Shelf.objects.get(pk=shelf_id)
    typeshelf = shelf.shelf_type.mediatype
    if request.method == 'POST':
        shelf = Shelf.objects.get(pk=shelf_id)
        if request.FILES: #should make this if form.cleaned_data['category'] != 'Text':
            form = AddMediaForm(request.POST, request.FILES)
            form.populatedisks(request.user)
        
            if form.is_valid():
                new_media = Media.objects.create(name=form.cleaned_data['name'],
                                            docfile = request.FILES['docfile'],
                                            description_body = form.cleaned_data['description_body'],
                                            description_excerpt = form.cleaned_data['description_excerpt'],
                                            user = request.user,
                                            disk = form.cleaned_data['disk'],
                                            size = request.FILES['docfile'].size,
                                            category = typeshelf,
                                            group = form.cleaned_data['group'],
                                            enable_comments = form.cleaned_data['enable_comments'],
                                            public = form.cleaned_data['public'])
                thedisk.space_used += new_media.size
                thedisk.space_left -= new_media.size
                thedisk.save()
                shelf.media.add(new_media)
                shelf.save()
                return HttpResponseRedirect(shelf.get_absolute_url())
                                            
        else:
            form = AddMediaForm(request.POST)
        
            if form.is_valid():
                new_media = Media.objects.create(name=form.cleaned_data['name'],
                                                description_body = form.cleaned_data['description_body'],
                                                description_excerpt = form.cleaned_data['description_excerpt'],
                                                user = request.user,
                                                disk = form.cleaned_data['disk'],
                                                size = '0',
                                                category = typeshelf,
                                                group = form.cleaned_data['group'],
                                                enable_comments = form.cleaned_data['enable_comments'],
                                                public = form.cleaned_data['public'])
                
        
                shelf.media.add(new_media)
                shelf.save()                            
                return HttpResponseRedirect(shelf.get_absolute_url())
        
            
    else:
        form = AddMediaForm({'name': 'Untitled'})
        
        
        #if request.user.username != username:
            #if request.user.is_authenticated:
    
        #if request.user.username is username:
        
        
    User = request.user
    form.fields['disk'].queryset = request.user.disk_set.all()
    shelfform = AddShelfForm(user=request.user)
    shelf = Shelf.objects.get(pk=shelf_id)
    user_library = {'user': User,
                        'user_shelfs': User.shelf_set.all(),
                        'form':shelfform,
                        'textform': form,
                        'theshelf':shelf}
                    
    return render_to_response('Library/addstuff.html', user_library, RequestContext(request, {}))
            
    
'''   
    return render_to_response('Media/add_media_form.html',
                                { 'form': form,
                                'disk_id':disk_id},
                                RequestContext(request, {}))'''
    
    
    
    

    
