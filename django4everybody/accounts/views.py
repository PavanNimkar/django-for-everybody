from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def custom_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")

        user = authenticate(
            request,
            username=username,
            password=password,
            confirm_password=confirm_password,
        )
        if user:
            login(request, user)
            return redirect("homepage")
        else:
            return render(request, "login.html", {"error": "Invalid credentials"})
    return render(request, "login.html")


def register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")

        if password != confirm_password:
            render(request, "register.html", {"error": "Password does not match"})

        if User.objects.all().filter(username=username).exists():
            render(request, "register.html", {"error": "Username alreday exits"})

        if User.objects.all().filter(email=email).exists():
            render(request, "register.html", {"error": "Email alreday exits"})

        user = User.objects.create_user(
            username=username, email=email, password=confirm_password
        )
        user.save()

        return redirect("login")

    return render(request, "register.html")


def show_users(request):
    users = User.objects.all()
    context = {"users": users}
    return render(request, "users.html", context)
