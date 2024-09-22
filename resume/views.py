from django.shortcuts import render

# Create your views here.

def home_view(request):
    return render(request, 'resume/base.html')

def resume_form(request):
    return render(request, "resume/resume_form.html")
