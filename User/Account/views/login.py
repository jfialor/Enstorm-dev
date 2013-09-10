
from django.contrib import auth
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect

def redirect(request):
    url = '/u/%s/' % request.user.username
    return HttpResponseRedirect(url)



#THIS IS NOT IN USE


def login(request):
    
    if request.method == 'POST':
        
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
    
        if user is not None and user.is_active:
            auth.login(request, user)
        
            return HttpResponseRedirect("/t/1/")
        
        else:
            return HttpResponseRedirect("/accounts/login/")
            
    else:
        form = loginform
        return render_to_response('Account/login.html')
    