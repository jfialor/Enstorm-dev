from django.shortcuts import get_object_or_404, render_to_response
from User.Creations.creationgroups.Media import Group
from Media.models import Media
from django.views.generic.list import ListView

def creation_home(request, username, disk_letter):
    #if request.user.username != username:
        #if request.user.is_authenticated:
    
    #if request.user.username is username:
    User = request.user
    disk = User.disk_set.get(letter__exact=disk_letter)
    user_library = { 'user': User,
                    'user_groups': User.group_set.all(),
                    'user_media': User.media_set.all(),
                    'user_disks': User.disk_set.all(),
                    'disk': disk,
                    'disk_media': disk.media_set.all()}
                    
    return render_to_response('Creations/home.html', user_library)
    

    
def creation_groups(request, username, group_id):
    user = request.user
    group = get_object_or_404(Group, pk=group_id)
    return render_to_response('Creations/groups.html', {'user' : user, 'media' : group.media_set.all(), 'another_media': Media.objects.filter(group_id=group.id)})

    
    
    
