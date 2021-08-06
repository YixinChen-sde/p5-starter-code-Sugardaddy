# chat/urls.py
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('chat', views.chat, name='chat'),
    path('activities', views.activities, name='activities'),
    path('days', views.days, name='days'),
    path('lovetracker', views.lovetracker, name='lovetracker'),
    path('share', views.share, name='share'),
    path('summary', views.summary, name='summary'),
    path('topics', views.topics, name='topics'),
    path('onetopic', views.onetopic, name='onetopic'),
    path('daysinput', views.daysinput, name='daysinput'),
    path('settings', views.settings, name='settings'),
    path('profile', views.profile, name='profile'),
    path('about', views.about, name='about'),
    path('randomTopics_one', views.randomTopics_one, name='randomTopics_one'),
    path('randomTopics_two', views.randomTopics_two, name='randomTopics_two')

]
