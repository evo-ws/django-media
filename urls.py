from django.conf.urls import patterns, url

from django_media import views

urlpatterns = patterns('',
    #url(r'^$', views.index, name='index'),
    url(r'^(?P<media_gallery_id>\d+)/$', views.view, name='view'),
)