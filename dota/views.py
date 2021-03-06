from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic  import View
from django.views.generic  import ListView
from dota.models  import Player

# Create your views here.

# Class based view to display a list of Model Player
class ListPlayersView(ListView):
    model = Player
    template_name = 'player_list.html'


# Home
def home(request):
    return HttpResponse("Home Page")


def player(request, player_id):
    response = "You are looking at player %s"
    return HttpResponse(response % player_id)


def match(request, match_id):
    response = "You are looking at match %s"
    return HttpResponse(response % match_id)


def detail(request, match):
    response = "You are looking at the details for match %s"
    return HttpResponse(response % match)
