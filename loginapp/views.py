from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from ecommerce import views
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required

# Create your views here.
def register(request):
    if request.method == 'GET':
        return render(request, 'loginapp/signup.html', {'form' : UserCreationForm()})
    
    # else is POST, so we create user
    else:
        if request.POST['password1'] == request.POST['password2']:
            # exception thrown if user creation fails. Username already exists
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('home')

            except IntegrityError:
                 return render(request, 'loginapp/signup.html', {'form': UserCreationForm(), 'error':'Username already exists. Please try again.'})
        else:
            return render(request, 'loginapp/signup.html', {'form': UserCreationForm(), 'error':'Passwords don\'t match, please try again.'})

def login_user(request):
    if request.method == 'GET':
        return render(request, 'loginapp/login.html', {'form' : AuthenticationForm()})
    
    # else is POST, login credentials are submitted
    else:
        # if user doesn't exist authenticate() will return none
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'loginapp/login.html', {'form' : AuthenticationForm(), 'error' : 'Username and Password don\'t match. Please try again.'})
        else:
            login(request, user)
            return redirect('home')
            
@login_required
def logout_user(request):
    if request.method == 'POST':
        logout(request)
        print('We here')
        # return redirect('signup')
        return redirect('home')