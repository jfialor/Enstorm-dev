from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from User.Account.models import SignupForm
from django.template import RequestContext
from django.core.context_processors import csrf
from User.Account.models import Disk
from User.Library.models import ShelfType, Shelf

def signup(request):

    if request.method == 'POST':
        form = SignupForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            shelftype = ShelfType.objects.get(name='Stack')
            Media_Disk = Disk.objects.create(letter='A',
                                            name= 'My Media',
                                            space_allocated='5368709120',
                                            space_used='0',
                                            space_left='5368709120',
                                            user = new_user)
            Archive_Disk = Disk.objects.create(letter='B',
                                            name= 'Archive',
                                            space_allocated='5368709120',
                                            space_used='0',
                                            space_left='5368709120',
                                            user = new_user)
            Stack = Shelf.objects.create(name='Stack',
                                    shelf_type=shelftype,
                                    user=new_user)
                                            
            return HttpResponseRedirect("/accounts/login/")
            #always redirect user after a POST
    else:
        form = SignupForm()
    return render_to_response('Account/signup.html',
                            { 'form': form },
                            RequestContext(request, {}))