from django.conf.urls import patterns, url
import views

urlpatterns = patterns('',
    url(r'^$', views.home, name='home'),
    url(r'^new/$', views.new, name='new'),
    url(r'^(?P<chat_id>.*?)/$', views.chat, name='chat'),
    )