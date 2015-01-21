from django.conf.urls import patterns,url
from notes import views

urlpatterns = patterns('notes.views',
    (r'^$', 'index'),
    (r'^new/$', 'new'),
)