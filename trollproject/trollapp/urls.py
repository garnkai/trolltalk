from django.urls import path, include
from trollapp import views
from django.contrib.auth.views import LoginView, LogoutView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("lobby/", views.lobby, name="lobby"),
 
    # login-section
    path("auth/login/", LoginView.as_view #changed
         (template_name="login.html"), name="login-user"), #changed
    path("auth/logout/", LogoutView.as_view(), name="logout-user"),
    path("auth/signup/", views.signup, name="signup"),
    path("race/", views.race, name="race"),


    # lobbies
    path('joinedLobby/<int:lobby_id>/', views.joinedLobby, name='joinedLobby'),

    path('create-lobby/', views.create_lobby_page, name='create-lobby-page'),
    path('create-lobby/action', views.create_lobby, name='create-lobby-action'),
]