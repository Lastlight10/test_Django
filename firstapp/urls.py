from django.urls import path

from . import views

urlpatterns = [
    path('', views.home_redirect, name='home'),
    path("login/", views.to_login, name="login"),
    path("user/", views.dashboard, name="dashboard"),
    path("login_user/", views.login_user, name="login_user"),
]