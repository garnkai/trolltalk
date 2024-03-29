from django.urls import path, include
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("lobby/", views.lobby, name="lobby"),
 
    # login-section
    path("accounts/login/", LoginView.as_view #changed
         (template_name="login.html"), name="login-user"), #changed
    path("auth/logout/", LogoutView.as_view(), name="logout-user"),
    path("race/<int:lobby_id>", views.race, name="race"),
    path("auth/signup/", views.signup, name="signup"),

    # lobbies
    path('joinedLobby/<int:lobby_id>/', views.joinedLobby, name='joinedLobby'),
    path('create-lobby/', views.create_lobby_page, name='create-lobby-page'),
    path('create-lobby/action', views.create_lobby, name='create-lobby-action'),
    path('race/get_lobby/<int:lobby_id>', views.get_lobby, name='get_lobby'),


    path('check_lobby/<int:lobby_id>/', views.check_lobby, name='check_lobby'),
    path('update_players_joined/<int:lobby_id>/', views.update_players_joined, name='update_players_joined'),
    path('race/get_lobby/<int:lobby_id>', views.get_lobby, name='get_lobby'),
]

