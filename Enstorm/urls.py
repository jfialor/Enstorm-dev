from django.conf.urls import patterns, include, url
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'Enstorm.mainviews.home', name='home'),
    # url(r'^Enstorm/', include('Enstorm.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^media/', include('Media.urls')),
    url(r'^(?P<disk_id>\d+)/addmedia/$', 'Media.views.addmedia', name='add_media'),
    url(r'^deletemedia/(?P<media_id>\d+)/$', 'Media.views.deletemedia', name='delete_media'),
    url(r'^u/', include('User.Account.urls')),
    url(r'^accounts/signup/', 'User.Account.views.signup.signup', name='signup'),
    #url(r'^accounts/login/', 'Artist.Account.views.login.login', name='login'),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login', 
                        {'template_name': 'Account/login.html'},
                         name='login'), #change redirect to send to allow to append username
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', 
                        {'template_name': 'Account/logout.html', 
                        #'next_page': '/accounts/login/'
                        },
                        name='logout'),
                        
    #(r'^static/(?P<path>.*)$', 'django.views.static.serve',
            #{'document_root': settings.STATIC_ROOT}),
    (r'^media/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT}),
    (r'^tiny_mce/(?P<path>.*)$', 'django.views.static.serve',)
    #{ 'document_root': '/Users/SedemFialor/documents/binary/Creation/static/js/tiny_mce/' }),
    #(r'^tinymce/', include('tinymce.urls')),
)
