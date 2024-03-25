from django.shortcuts import render, redirect
from .models import Lobby, LinesForTyping
from django.db import IntegrityError
from django.http import JsonResponse



def homepage(request):
    return render(request, "homepage.html")
def lobby(request): # Added function
    if not request.user.is_authenticated:
        return redirect("login-user")
    lobbies = Lobby.objects.all()  # Retrieve all lobbies
    context = {'lobbies': lobbies}
    return render(request, "lobby.html", context) # changed

def race(request, lobby_id):

    return render(request, 'race.html',)

# rooms
def joinedLobby(request, lobby_id):
    #lobby_id = request.GET.get('lobby_id')


    #return render(request, "lobby1.html")
    #return render(request, "joinedLobby.html", {"lobby_id": lobby_id})
    try:
        lobby = Lobby.objects.get(id=lobby_id)
        lobby_name = lobby.lobby_name
    except Lobby.DoesNotExist:
        lobby_name = None
        

    return render(request, "joinedLobby.html", {"lobby_id": lobby_id, "lobby_name": lobby_name})
    

# Create lobby
def create_lobby_page(request):
    return render(request, 'create_lobby.html')

def create_lobby(request):
    error_message = None
    if request.method == 'POST':
        lobby_name = request.POST.get('lobby_name')
        num_players = request.POST.get('num_players')
        game_mode = request.POST.get('game_mode')
        privacy = request.POST.get('privacy')
        
        # Error where lobby name can already exist in a model,
        # so it cannot be create because name must be unique

        try:
            existing_lobby = Lobby.objects.get(lobby_name=lobby_name)
        except Lobby.DoesNotExist:
            # If lobby name is not taken, create a lobby model instance
            lobby = Lobby.objects.create(
                lobby_name=lobby_name,
                num_players=num_players,
                game_mode=game_mode,
                privacy=privacy
            )
            # Go to the joined lobby with the lobby id of the lobby just created
            return redirect('joinedLobby', lobby_id=lobby.id)
        except IntegrityError:
            error_message = "Name is taken, try again"

    # the error alert does not work im not sure why
    return render(request, 'create_lobby.html', {'error_message': error_message})

def get_lobby(request, lobby_id):
    #gets lobby's id
    lobby = Lobby.objects.get(id=lobby_id)

    #gets its game mode
    lobbyType =lobby.game_mode

    #gets lines that belong to the gamemode
    lines = list(LinesForTyping.objects.filter(Character=lobbyType).values('Line'))
    return JsonResponse(lines, safe=False)