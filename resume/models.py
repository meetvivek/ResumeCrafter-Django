from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


    # Personal Information
    full_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    location = models.CharField(max_length=100)

    linkedin = models.CharField(blank=True, null=True, max_length=100)
    github = models.CharField(blank=True, null=True, max_length=100)
    portfolio = models.URLField(blank=True, null=True)
    leetcode = models.URLField(blank=True, null=True)
    gfg = models.URLField(blank=True, null=True)
    hackerrank = models.URLField(blank=True, null=True)
    hackerearth = models.URLField(blank=True, null=True)
    other_link = models.URLField(blank=True, null=True)
    
    summary = models.TextField(default="Your Summary")

    # 10th Education
    institution_10 = models.CharField(max_length=100, blank=True, null=True)
    institution_10_location = models.CharField(max_length=100, blank=True, null=True)
    degree_10 = models.CharField(max_length=200, blank=True, null=True)
    end_year_10 = models.IntegerField(blank=True, null=True)
    board_10 = models.CharField(max_length=100, blank=True, null=True)
    grade_type_10 = models.CharField(max_length=15, blank=True, null=True)
    percentage_10 = models.FloatField(blank=True, null=True)
    
    # 12th Education
    institution_12 = models.CharField(max_length=100)
    institution_12_location = models.CharField(max_length=100, default="xyz")
    degree_12 = models.CharField(max_length=200)
    end_year_12 = models.IntegerField(default="2024")
    board_12 = models.CharField(max_length=100)
    grade_type_12 = models.CharField(max_length=15, blank=True, null=True)
    percentage_12 = models.FloatField(blank=True, null=True)

    # Graduation Education
    college = models.CharField(max_length=100)
    college_location = models.CharField(max_length=100, default="xyz")
    degree_college = models.CharField(max_length=200)
    specialization = models.CharField(max_length=200)
    start_year_college = models.IntegerField(default=2021)
    end_year_college = models.IntegerField(default=2024)
    grade_type_college = models.CharField(max_length=15, blank=True, null=True)
    percentage_college = models.FloatField(blank=True, null=True)

    
    # Skills
    languages = models.CharField(max_length=500)
    frameworks = models.CharField(max_length=500, blank=True, null=True)
    other_skills = models.CharField(max_length=500, blank=True, null=True)
    
    # Projects
    project_title_1 = models.CharField(max_length=100)
    project_description_1  = models.TextField()
    technologies_used_1  = models.CharField(max_length=200)
    project_link_1  = models.URLField(blank=True, null=True)

    # Projects
    project_title_2 = models.CharField(max_length=100, blank=True, null=True)
    project_description_2 = models.TextField(blank=True, null=True)
    technologies_used_2 = models.CharField(max_length=200, blank=True, null=True)
    project_link_2 = models.URLField(blank=True, null=True)

    # Work Experience 1
    job_title_1 = models.CharField(max_length=100, blank=True, null=True)
    job_mode_1 =  models.CharField(max_length=100, blank=True, null=True)
    company_name_1 = models.CharField(max_length=100, blank=True, null=True)
    start_date_1 = models.DateField(blank=True, null=True)
    end_date_1 = models.DateField(blank=True, null=True)
    job_description_1 = models.TextField(blank=True, null=True)

    # Work Experience 2
    job_title_2 = models.CharField(max_length=100, blank=True, null=True)
    job_mode_2 = models.CharField(max_length=100, blank=True, null=True)
    company_name_2 = models.CharField(max_length=100, blank=True, null=True)
    start_date_2 = models.DateField(blank=True, null=True)
    end_date_2 = models.DateField(blank=True, null=True)
    job_description_2 = models.TextField(blank=True, null=True)
    

    # Awards and Achievements
    award = models.TextField(max_length=2000, blank=True, null=True)
    
    # Certifications
    certifications = models.TextField(max_length=2000, blank=True, null=True)

    def __str__(self):
        return self.user.username
