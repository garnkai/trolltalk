from django.urls import path, include
from trollapp import views
from django.contrib.auth.views import LoginView, LogoutView
 
urlpatterns = [
    path("", views.lobby, name="lobby"),
 
    # login-section
    path("auth/login/", LoginView.as_view #changed
         (template_name="login.html"), name="login-user"), #changed
    path("auth/logout/", LogoutView.as_view(), name="logout-user"),
]