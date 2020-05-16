from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.db import IntegrityError

def signupuser(request):
    if request.method == 'GET':
        return render(request, 'accounts/signup.html', {'form': UserCreationForm})
    else:
        if (request.POST['password1'] == request.POST['password2']) and request.POST['password1'] != '':
            try:
                new_user = User.objects.create_user(request.POST['username'], None,request.POST['password1'])
                new_user.save()
                login(request, new_user)
                return redirect('home')
            except IntegrityError:
                return render(request, 'accounts/signup.html', {'form': UserCreationForm, 'error': 'Incorrect data'})
        else:
            return render(request, 'accounts/signup.html', {'form': UserCreationForm, 'error': 'Username or password is not correct'})

def loginuser(request):
    if request.method == 'GET':
        return render(request, 'accounts/login.html', {'form': AuthenticationForm})
    else:
        auth = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if not auth:
            return render(request, 'accounts/login.html', {'form': AuthenticationForm, 'error': 'Username or password incorrect'})
        else:
            login(request, auth)
            return redirect('home')

def logooutuser(request):
    logout(request)
    return redirect('home')