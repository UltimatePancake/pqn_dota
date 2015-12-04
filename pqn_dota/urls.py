"""pqn_dota URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView
import dota.views


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^players/',  dota.views.ListPlayersView.as_view(),name='player_list',),
    url(r'^player/(?P<player_id>[0-9]+)/', dota.views.player, name='player'),
    url(r'^match/(?P<match_id>[0-9]+)/', dota.views.match, name='match'),
    url(r'^detail/(?P<match>[0-9]+)/', dota.views.detail, name='detail'),
]
