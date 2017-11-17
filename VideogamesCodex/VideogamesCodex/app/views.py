"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from app.models import Game
from django.http import HttpResponseRedirect
from app.forms import GameForm
from django.template import RequestContext

#HOME
def home(request):
    games = Game.objects.all()
    return render(request,
        'app/index.html',
        {
            "title" : "Game List",
            "games" : games,
        })
#VER
def show_game(request, id):
    game = Game.objects.get(pk=id)
    return render(request,
                 'app/show.html',
                 { "game" : game })

#CREAR
def create_game(request):
    if request.method == 'POST':
               
        formulario = GameForm(request.POST)
        if formulario.is_valid():
            
            game = formulario.save()
            return HttpResponseRedirect('/show/' + str(game.id))

    elif request.method == 'GET':
      
        formulario = GameForm()
        return render(request,
                    'app/gameform.html',
                    { 'form' : formulario,
                      'action': "/create"})
    else:
        return render(request, 'app/404.html')

    #Modificar
def edit_game(request, id):

    game = Game.objects.get(pk=id)
    if request.method == 'POST':
        formulario = GameForm(request.POST, instance=game)
        if formulario.is_valid():
            game = formulario.save()
            return HttpResponseRedirect("/show/" + str(game.id))

    elif request.method == 'GET':
        formulario = GameForm(instance = game)
        return render(request,
                      'app/gameform.html',
                      {'form': formulario,
                       'action' : '/show/' + str(game.id)})
    else:
        return render(request, 'app/404.html')


    #BORRAR
def remove_game(request, id):
    game = Game.objects.get(pk=id)
    game.delete()
    return HttpResponseRedirect('/') 
#RANKING
def ranking(request):
    games = Game.objects.values_list("name", "score").order_by("score").reverse
    return render(request,
        'app/ranking.html',
        {
            "title" : "Game List",
            "games" : games,
        })

#ERROR 
def not_found(request):
    return render(request, 'app/404.html')