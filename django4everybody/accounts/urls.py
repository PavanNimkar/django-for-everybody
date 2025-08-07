from django.urls import path
from . import views

urlpatterns = [
    path("", views.show_users, name="show_users"),
    path("login/", views.custom_login, name="login"),
    path("register/", views.register, name="register"),
]
