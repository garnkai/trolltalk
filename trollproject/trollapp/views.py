from django.shortcuts import render, redirect

def lobby(request): # Added function
    if not request.user.is_authenticated:
        return redirect("login-user")
    context = {}
    return render(request, "lobby.html", context) # changed

