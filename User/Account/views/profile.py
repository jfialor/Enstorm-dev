from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render_to_response
from django.views.generic.list import ListView


def user_home(request, username):
    #if request.user.username = username
    return render_to_response('user_detail.html', {'user' : request.user})
