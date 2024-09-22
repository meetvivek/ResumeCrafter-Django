from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

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

def home_view(request):
    return render(request, 'resume/base.html')

def resume_form(request):
    return render(request, "resume/resume_form.html")
