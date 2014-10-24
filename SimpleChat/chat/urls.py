from django.conf.urls import patterns, url
import views

urlpatterns = patterns('',
    url(r'^$', views.home, name='home'),
    url(r'^new/$', views.new, name='new'),
    url(r'^json/new/$', views.json_new, name='json_new'),
    url(r'^json/(?P<chat_id>.*?)/$', views.json_chat, name='json_chat'),
    url(r'^(?P<chat_id>.*?)/$', views.chat, name='chat'),

    )