from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response

def home(request):
    if request.user.is_authenticated():
        user_homepage = '/u/%s/' %(request.user.username)
        return HttpResponseRedirect(user_homepage)
    
    else:
        return render_to_response('home.html')
    