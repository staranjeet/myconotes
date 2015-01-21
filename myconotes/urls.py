from django.conf.urls import patterns, include, url
from django.contrib import admin
from notes import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myconotes.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^notes/', include('notes.urls')),
    url(r'^$','notes.views.index',name='index'),
    url(r'^newurl/$','notes.views.newurl',name='newurl'),
    url(r'^notes/(?P<url>[\w.@+-,\' \'\';\'%{}\[\]]+)/?$','notes.views.viewnotes',name='viewnotes'),
    url(r'^deletenote$','notes.views.deletenote',name='deletenote'),
    url(r'^savenote/$','notes.views.savenote',name='savenote'),
    url(r'^admin/', include(admin.site.urls)),
)
