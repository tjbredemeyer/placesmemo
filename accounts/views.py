'''Views for accounts app'''
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import UserRegistrationForm

def login_view(request):
    '''Login view'''
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('places')
        messages.error(request, 'Invalid username or password.')
    return render(request, 'login.html')


def logout_view(request):
    '''Logout view'''
    logout(request)
    return redirect('home')


def register(request):
    '''Register view'''
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})
