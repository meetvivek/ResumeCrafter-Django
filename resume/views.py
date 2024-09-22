from django.shortcuts import render, redirect
from .models import Profile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError

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
    if request.method == 'POST':
        profile_data = {
            'full_name': request.POST.get('full_name'),
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


            'college': request.POST.get('college'),
            'college_location': request.POST.get('college_location'),
            'degree_college': request.POST.get('degree_college'),
            'specialization': request.POST.get('specialization'),
            'start_year_college': request.POST.get('start_year_college'),
            'end_year_college': request.POST.get('end_year_college'),
            'grade_type_college': request.POST.get('grade_type_college'),
            'percentage_college': request.POST.get('percentage_college') or None,

            # Skills (renamed from `skill_name`)

            'languages': request.POST.get('languages'),
            'frameworks': request.POST.get('frameworks'),
            'other_skills': request.POST.get('other_skills'),

            # Projects
            'project_title_1': request.POST.get('project_title_1'),
            'project_description_1': request.POST.get('project_description_1'),
            'technologies_used_1': request.POST.get('technologies_used_1'),
            'project_link_1': request.POST.get('project_link_1')
            ,
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
        # Profile.objects.create(**profile_data)
        # return redirect('resumes')

        user = request.user

        try:
            # Update or create the UserData object
            user_data, created = Profile.objects.update_or_create(
                user=user,
                defaults=profile_data
            )
            # Redirect to a success page or another URL
            return redirect('home')  # Replace 'success_url' with your actual success URL
        
        except IntegrityError as e:
            # Handle database integrity error (e.g., unique constraint violations)
            print("Error saving data:", e)
            return render(request, 'resume/resume_form.html', {'error': 'There was an error saving your data. Please try again.'})

    return render(request, "resume/resume_form.html")
