from django.views.generic.detail import DetailView
from django.conf.urls import patterns, include, url
from models import Media

media_info = { 'queryset': Media.objects.all()}

urlpatterns = patterns('',
        url(r'^(?P<pk>\d+)/$', DetailView.as_view(**media_info), name='media_detail'),

)