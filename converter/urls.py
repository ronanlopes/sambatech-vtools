from django.conf.urls import patterns, url

from converter import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
)
