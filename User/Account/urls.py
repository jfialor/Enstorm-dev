from django.conf.urls import patterns, include, url
from django.views.generic.detail import DetailView
from django.contrib.auth.models import User


urlpatterns = patterns('',
        url(r'^$', 'User.Account.views.login.redirect'),
        url(r'^(?P<username>[-\w]+)/$', 'User.Account.views.profile.user_home', name='user_homepage'),
        
        url(r'^(?P<username>[-\w]+)/library/$', 'User.Library.views.library_home', name='user_library_home'),
        url(r'^(?P<username>[-\w]+)/library/newshelf$', 'User.Library.views.internewshelf', name='internewshelf'),
        url(r'^(?P<username>[-\w]+)/library/(?P<shelf_id>[-\w]+)$', 'User.Library.views.library_shelf', name='user_library_shelf'),
        url(r'^(?P<username>[-\w]+)/library/addshelf/$', 'User.Library.views.add_shelf', name='add_shelf'),
        url(r'^(?P<username>[-\w]+)/library/(?P<shelf_id>[-\w]+)/newmedia/$', 'User.Library.views.newmedia', name='new_media'),
        url(r'^(?P<username>[-\w]+)/library/(?P<shelf_id>[-\w]+)/(?P<media_id>[-\w]+)/$', 'User.Library.views.mediaview', name='media_view'),
        
        
        
        url(r'^(?P<username>[-\w]+)/shelve/(?P<media_id>[-\w]+)/$', 'User.Library.views.intershelve', name='intershelve'),
        url(r'^(?P<username>[-\w]+)/shelve/(?P<media_id>[-\w]+)/(?P<shelf_id>[-\w]+)/$', 'User.Library.views.shelve', name='shelve'),
        
        #url(r'^(?P<username>[-\w]+)/library/shelf/$', 'Artist.Library.views.library_shelf', name='user_library_shelf'), #list of shelfs
        #url(r'^(?P<username>[-\w]+)/library/gallery/$', 'Artist.Library.views.library_gallery', name='user_library_gallery'), #list of galleries
        #url(r'^(?P<username>[-\w]+)/library/musicplaylist/$', 'Artist.Library.views.library_musicplaylist', name='user_library_musicplaylist'), #list of playlists
        #url(r'^(?P<username>[-\w]+)/library/videoplaylist/$', 'Artist.Library.views.library_videoplaylist', name='user_library_videoplaylist'), #list of playlists1
        
        #now make views for particular shelfs and particular galleries and such
        
        url(r'^(?P<username>[-\w]+)/database/(?P<disk_letter>[-\w]+)/$', 'User.Creations.views.creationpages.creation_home', name='user_creation_home'),
        url(r'^(?P<username>[-\w]+)/creations/group/(?P<group_id>[-\w]+)/$', 
                'User.Creations.views.creationpages.creation_groups', name='user_creation_groups'),

        url(r'^(?P<username>[-\w]+)/(?P<disk_letter>[-\w]+)/addgroup/$', 
                'User.Creations.views.creationforms.addgroup', name='user_creation_groups'),
)


"""
        url(r'^(?P<username>[-\w]+)/creations/mypamphlet/$', 'Artist.Creations.views.creation_pamphlets', name='user_library_shelf'), #list of shelfs
        url(r'^(?P<username>[-\w]+)/creations/myportfolio/$', 'Artist.Creations.views.creation_portfolios', name='user_library_gallery'), #list of galleries
        url(r'^(?P<username>[-\w]+)/creations/mymusicplaylist/$', 'Artist.Creations.views.creation_musicplaylists', name='user_library_musicplaylist'), #list of play
        url(r'^(?P<username>[-\w]+)/creations/myvideoplaylist/$', 'Artist.Creations.views.creation_videoplaylists', name='user_library_videoplaylist'), #list of playlis

)
"""