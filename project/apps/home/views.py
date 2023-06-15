from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView



def index(request):
    return render (request, "home/index.html")

def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request.POST, data = request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get("username")
            contraseña = form.cleaned_data.get("password")
            user = authenticate(username = usuario, password = contraseña)
            if user is not None:
                login(request, user)
                return render(request, "home/index.html")
    else:
        form = AuthenticationForm()
    return render(request, "home/login.html", {"form" : form})   


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            form.save()
            return render(request, "home/index.html")
    else:
        form = UserCreationForm()
    return render(request, "home/register.html", {"form" : form})            






        