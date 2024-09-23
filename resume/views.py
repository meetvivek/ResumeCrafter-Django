from django.shortcuts import render, redirect, get_object_or_404
from .models import Profile
from .forms import RegisterForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
import pdfkit
from django.template import loader
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.utils import timezone

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username').lower()
            messages.success(request, f"Congrats, {username}! Your account has been successfully crafted.")
            return redirect('login')
    else:
        form = RegisterForm()
    first_error = None
    if form.errors:
        first_error = next(iter(form.errors.values()))[0] if form.errors else None
    return render(request, 'resume/register.html', {'form': form, 'first_error': first_error})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f"Welcome, {username}! Let's get crafting that perfect resume!")
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
    return render(request, 'resume/home.html')


@login_required
def resume_form(request):
    if request.method == 'POST':
        profile_data = {
            'full_name': request.POST.get('full_name'),
            'date': timezone.now(),  # Current date
            'email': request.POST.get('email'),
            'phone_number': request.POST.get('phone_number'),
            'linkedin': request.POST.get('linkedin'),
            'github': request.POST.get('github'),
            'portfolio': request.POST.get('portfolio'),
            'location': request.POST.get('location'),
            'summary': request.POST.get('summary'),
            'leetcode': request.POST.get('leetcode'),
            'gfg': request.POST.get('gfg'),
            'hackerrank': request.POST.get('hackerrank'),
            'hackerearth': request.POST.get('hackerearth'),
            'other_link': request.POST.get('other_link'),

            # Education fields 10
            'institution_10': request.POST.get('institution_10'),
            'institution_10_location': request.POST.get('institution_10_location'),
            'degree_10': request.POST.get('degree_10'),
            'end_year_10': request.POST.get('end_year_10') or None,
            'board_10': request.POST.get('board_10'),
            'grade_type_10': request.POST.get('grade_type_10'),
            'percentage_10': request.POST.get('percentage_10') or None,

            # Education fields 12
            'institution_12': request.POST.get('institution_12'),
            'institution_12_location': request.POST.get('institution_12_location'),
            'degree_12': request.POST.get('degree_12'),
            'end_year_12': request.POST.get('end_year_12') or None,
            'board_12': request.POST.get('board_12'),
            'grade_type_12': request.POST.get('grade_type_12'),
            'percentage_12': request.POST.get('percentage_12') or None,

            # College
            'college': request.POST.get('college'),
            'college_location': request.POST.get('college_location'),
            'degree_college': request.POST.get('degree_college'),
            'specialization': request.POST.get('specialization'),
            'start_year_college': request.POST.get('start_year_college'),
            'end_year_college': request.POST.get('end_year_college'),
            'grade_type_college': request.POST.get('grade_type_college'),
            'percentage_college': request.POST.get('percentage_college') or None,

            # Skills
            'languages': request.POST.get('languages'),
            'frameworks': request.POST.get('frameworks'),
            'other_skills': request.POST.get('other_skills'),

            # Projects
            'project_title_1': request.POST.get('project_title_1'),
            'project_description_1': request.POST.get('project_description_1'),
            'technologies_used_1': request.POST.get('technologies_used_1'),
            'project_link_1': request.POST.get('project_link_1'),
            'project_title_2': request.POST.get('project_title_2'),
            'project_description_2': request.POST.get('project_description_2'),
            'technologies_used_2': request.POST.get('technologies_used_2'),
            'project_link_2': request.POST.get('project_link_2'),

            # Work Experience
            'job_title_1': request.POST.get('job_title_1'),
            'job_mode_1': request.POST.get('job_mode_1'), 
            'company_name_1': request.POST.get('company_name_1'),
            'start_date_1': request.POST.get('start_date_1') or None,
            'end_date_1': request.POST.get('end_date_1') or None,
            'job_description_1': request.POST.get('job_description_1'), 

            'job_title_2': request.POST.get('job_title_2'),
            'job_mode_2': request.POST.get('job_mode_2'),  
            'company_name_2': request.POST.get('company_name_2'),
            'start_date_2': request.POST.get('start_date_2') or None,
            'end_date_2': request.POST.get('end_date_2') or None,
            'job_description_2': request.POST.get('job_description_2'),  

            'award': request.POST.get('award'), 
            'certifications': request.POST.get('certifications')  
        }

        user = request.user

        try:
            # Create a new profile for the user
            Profile.objects.create(user=user, **profile_data)
            return redirect('resumes')  # Replace 'resumes' with your actual redirect URL

        except IntegrityError as e:
            print("Error saving data:", e)
            return render(request, 'resume/resume_form.html', {'error': 'There was an error saving your data. Please try again.'})

    return render(request, "resume/resume_form.html")

@login_required
def delete_profile(request, profile_id):
    # Get the profile by id and make sure it belongs to the logged-in user
    profile = get_object_or_404(Profile, id=profile_id, user=request.user)

    if request.method == 'POST':
        # Delete the profile instance
        profile.delete()
        messages.success(request, "Profile deleted successfully.")
        return redirect('resumes')  # Redirect to the list of resumes or another relevant page

    return render(request, 'resume/delete_confirm.html', {'profile': profile})

def resume(request, id):
    user_profile = Profile.objects.get(pk=id)
    template = loader.get_template('resume/resume_template.html')
    html = template.render({'user_profile': user_profile})

    options = {
        'page-size': 'Letter',
        'encoding': 'UTF-8',
        'margin-top': '12mm',  
        'margin-right': '5mm',  
        'margin-bottom': '0mm', 
        'margin-left': '5mm',   
    }
    pdf = pdfkit.from_string(html, False, options)
    
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="resume.pdf"'
    
    return response

@login_required
def view_resumes(request):
    profiles = Profile.objects.filter(user=request.user)
    return render(request, "resume/view_resumes.html", {'profiles': profiles})