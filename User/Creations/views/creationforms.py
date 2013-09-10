from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.contrib.auth.models import User
from User.Creations.forms import AddGroupForm
from django.forms import ModelForm
from User.Creations.creationgroups.Media import Group
from User.Account.models import Disk

'''
class PamphletForm(ModelForm):
    class Meta:
        model = MyTextPamphlet
        #exclude = ['artist']
'''

                            
def addgroup(request, username, disk_letter):
    user = User.objects.get(username=username)
    disk = Disk.objects.get(letter=disk_letter, user=user )
    if request.method == 'POST':
        form = AddGroupForm(user=request.user, thedisk = disk, data=request.POST)
        #form = PamphletForm(data=request.POST)
        if form.is_valid():
            new_group = form.save()#.save(commit=False)
            #new_pamphlet.artist = request.user
            return HttpResponseRedirect(new_group.get_absolute_url())
        
    else:
        form = AddGroupForm(user=request.user, thedisk = disk)
    return render_to_response('Creations/add_group_form.html', 
                            { 'form':form },
                            RequestContext(request, {}))