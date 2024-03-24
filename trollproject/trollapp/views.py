from django.shortcuts import render, redirect

def homepage(request):
    return render(request, "homepage.html")
def lobby(request): # Added function
    if not request.user.is_authenticated:
        return redirect("login-user")
    context = {}
    return render(request, "lobby.html", context) # changed

def race(request):
    return render(request, "race.html")