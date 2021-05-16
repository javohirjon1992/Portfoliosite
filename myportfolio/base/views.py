from django.shortcuts import render
from .models import *
# Create your views here.
def home(request):
    logo = Logo.objects.all()
    navmenu = NavbarMenu.objects.all()
    skills = Home.objects.all()
    social_logo = SocialLink.objects.all()
    about_detail = About.objects.all()
    interest = Interest.objects.all()
    result_image = Result.objects.all()
    result_total = ResultOutcome.objects.all()
    services_title = ServicesTitle.objects.all()
    services_name = ServiceMain.objects.all()
    work_participation = WorkPart.objects.all()
    work_part_detail = WorkPartDetail.objects.all()
    work_expert = WorkExpertise.objects.all()
    your_profession = Profession.objects.all()
    your_skills = YourSkills.objects.all()

    



    context = {'logo': logo, 'navmenu': navmenu, 
    'skills': skills, 'social_logo': social_logo, 'about_detail': about_detail, 
    'interest': interest, 'result_total': result_total, 'result_image': result_image,
    'service_title': services_title, 'service_name': services_name,
    'work_participation': work_participation, 'work_part_detail': work_part_detail,
    'work_expert': work_expert,
    'your_profession': your_profession,
    'your_skills': your_skills,


    
    }
    return render(request, 'base/index.html', context)
    

def services(request):
    return render(request, 'base/services.html')

def resume(request):
    return render(request, 'base/resume.html')

def projects(request):
    return render(request, 'base/projects.html')

def blog(request):
    return render(request,'base/blog.html')

def contact(request):
    return render(request, 'base/contact.html')

def test(request):
    skills = Home.objects.all()
    context = { 'skills': skills, }
    return render(request, 'base/test.html', context)
    

