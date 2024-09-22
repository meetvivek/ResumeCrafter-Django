from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserCreationForm(request.POST)
    return render(request, 'resume/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            # Invalid login credentials
            context = {'error': 'Invalid username or password'}
            return render(request, 'resume/login.html', context)
    return render(request, 'resume/login.html')

@login_required
def logout_view(request):
    logout(request)
    return redirect('home')

def home_view(request):
    return render(request, 'resume/base.html')

def resume_form(request):
    return render(request, "resume/resume_form.html")
