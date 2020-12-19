from django.shortcuts import render, redirect, resolve_url
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import Registration

# Create your views here.


def user_login (request) :
    if request.user.is_authenticated:
        return redirect('main:home')
    form = Registration()
    if request.method == "POST" :
        if request.POST.get('Login', False) == 'Login':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username = username, password = password)
            if user is not None:
                login(request, user)
                return redirect('main:home')
            else:
                messages.error(request, "Username or Password is incorrect")
        elif request.POST.get('Sign Up', False) == 'Sign Up':
                form = Registration(request.POST)
                if form.is_valid():
                    form.save()
                    user = form.cleaned_data.get('username')
                    messages.success(request, 'Account was created for ' + user)
                    username = request.POST['username']
                    password = request.POST['password1']
                    user = authenticate(request, username = username, password = password)
                    login(request, user)
                    return redirect('main:home')

    context = {}
    return render(request, 'userauth/userauth.html', context)

def user_logout(request):
    logout(request)
    return redirect(resolve_url('userauth:login'))