from django.shortcuts import render, redirect
from .models import Lobby, LinesForTyping
from django.db import IntegrityError
from django.http import JsonResponse

from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from .models import Lobby
from django.db import IntegrityError

from django.http import JsonResponse

from django.contrib.auth.decorators import login_required
from .forms import *

@login_required

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
        # so it cannot be created because name must be unique

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
    

# Function to check if lobby with id exists or not, returns a bool
def check_lobby(request, lobby_id):
    if Lobby.objects.filter(id=lobby_id).exists():
        return JsonResponse({'exists': True})
    else:
        return JsonResponse({'exists': False})

# function to increase player count by one
'''
def increase_players_joined(request, lobby_id):
    try:
        lobby = Lobby.objects.get(id=lobby_id)
        lobby.playersJoined += 1
        lobby.save()
        return JsonResponse({'success': True})
    except Lobby.DoesNotExist:
        return JsonResponse({'success': False})'''

# I also need to decrease, so instead change the function to update
# the player count instead, allowing both increasing and decreasing
def update_players_joined(request, lobby_id, action):
    try:
        lobby = Lobby.objects.get(id=lobby_id)
        if action == 'increase':
            lobby.playersJoined += 1
        elif action == 'decrease':
            lobby.playersJoined -= 1
            # Make sure the player count doesnt go less than 0, 
            # placeholder because when the count is 0 the model should delete
            if lobby.playersJoined < 0:
                lobby.playersJoined = 0
        lobby.save()
        return JsonResponse({'success': True})
    except Lobby.DoesNotExist:
        return JsonResponse({'success': False})

def get_lobby(request, lobby_id):
    #gets lobby's id
    lobby = Lobby.objects.get(id=lobby_id)
    #gets its game mode
    lobbyType =lobby.game_mode
    #gets lines that belong to the gamemode
    lines = list(LinesForTyping.objects.filter(Character=lobbyType).values('Line'))
    return JsonResponse(lines, safe=False)

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('homepage')
    else:
       if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
       return render(request, 'login.html')

def signup(request):
    if request.method == 'POST':
        form = createuserform(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('login-user')
    else:
        form = createuserform()
    return render(request, 'signup.html', {'form': form})
