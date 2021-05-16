from django.db import models
from django.db.models.fields import IntegerField

# Create your models here.
#this is Logo model     start
class Logo(models.Model):
    user = models.CharField(max_length=200, null=True, verbose_name="Your Logoname",)
    logo_picture = models.ImageField(null=True, blank=True, verbose_name="Your Logo picture: File type: \"jpg or png\"", upload_to='logoimages/')
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    def __str__(self):
        return self.user 
## Logo model end
class SocialLink(models.Model):
    social_name = models.CharField(max_length=100, null=True, verbose_name="Social name" )
    social_class = models.CharField(max_length=255, null=True, verbose_name="Social icon as Material Design Icons class" )
    social_link = models.CharField(max_length=255, null=True, verbose_name="Social Link" )
    def __str__(self):
        return self.social_name
##Navbar menu model Start

class NavbarMenu(models.Model):
    menu_name = models.CharField(max_length=20, null=True, verbose_name="Menu name")
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    def __str__(self):
        return self.menu_name


class Home(models.Model):
    title_skills = models.CharField(max_length=255, null=True, verbose_name="Skills")
    full_name = models.CharField(max_length=255, null=True, verbose_name="Full name")
    about_us = models.TextField(max_length=1000, null=True, verbose_name="About my skills")
    home_picture = models.ImageField(null=True, blank=True, verbose_name="Your picture: File type: \"jpg or png\": Size 2000x1333 pixels", upload_to='homeimages/')
    your_cv = models.FileField(null=True, blank=True, verbose_name="Your CV: File type: \"pdf or doc\"", upload_to='cv/')
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    def __str__(self):
        return self.title_skills


class About(models.Model):
    full_name = models.CharField(max_length=255, null=True, verbose_name='Name and Surname' )
    about_us = models.CharField(max_length=200, null=True, verbose_name='About your talent' )
    about_prof = models.CharField(max_length=200, null=True, verbose_name='About your Profession' )
    about_more = models.TextField(max_length=2500, null=True, verbose_name='About your skills write detail' )
    your_sign = models.ImageField(null=True, blank=True, verbose_name="Your sign: File type:  \"jpg or png\": Size 182x57 pixels "  , upload_to='sign/')
    your_picture = models.ImageField(null=True, blank=True, verbose_name="Your picture: File type: \"jpg or png\" Size 600x786 pixels  ", upload_to='picture/')
    your_hobbi = models.CharField(max_length=255, null=True, verbose_name='About your hobbi Title' )
    your_hobbi_detail = models.TextField(max_length=2500, null=True, verbose_name='About your hobbi Detail' )

    def __str__(self):
        return self.full_name

class Interest(models.Model):
    your_interest_title = models.CharField(max_length=255, null=True, verbose_name='About your interest class for Feathericon class ' )
    your_interest_detail = models.CharField(max_length=55, null=True, verbose_name='About your interest skills' )
    
    def __str__(self):
        return self.your_interest_detail


class Result(models.Model):
    result_image = models.ImageField(null=True, blank=True, verbose_name="Your result background image: File type:  \"jpg or png\": Size 2000x800 pixels "  , upload_to='resultbackground/')
    
    

class ResultOutcome(models.Model):
    result_class = models.CharField(max_length=200, null=True, verbose_name='Your result  class for Feathericon class')
    result_total =  models.IntegerField(null=True, verbose_name='Your total  result  number' )
    result_name = models.CharField(max_length=200, null=True, verbose_name='Your result name')
    def __str__(self):
        return self.result_name

class ServicesTitle(models.Model):
    services_title_main = models.CharField(max_length=255, null=True, verbose_name='Your services main Title')
    services_title = models.TextField(max_length=10000, null=True, verbose_name='Your services detail')

    def __str__(self):
        return self.services_title_main

class ServiceMain(models.Model):
    service_class = models.CharField(max_length=200, null=True, verbose_name='Your services  class for Feathericon class')
    service_name = models.CharField(max_length=200, null=True, verbose_name='Your services name')
    service_detail = models.TextField(max_length=2000, null=True, verbose_name='Your services  detail')

    def __str__(self):
        return self.service_name


class WorkPart(models.Model):
    work_part = models.CharField(max_length = 255, null = True, verbose_name = 'Work participation' )
    work_part_detail = models.TextField(max_length = 3000, null = True, verbose_name = 'Work participation detail' )

    def __str__(self):
        return self.work_part

class WorkPartDetail(models.Model):
    begin_work = models.DateField(auto_now=False, auto_now_add=False, verbose_name='Begin work date')
    end_work = models.DateField(auto_now=False, auto_now_add=False, verbose_name='End work date')
    company_name = models.CharField(max_length =255, null =True, verbose_name='Company name')
    your_position = models.CharField(max_length =255, null =True, verbose_name='Your company position')
    name_skills = models.CharField(max_length =255, null =True, verbose_name='Your position in the company ')
    complete_projects = models.TextField(max_length=1500, null=True,verbose_name = 'Write in detail about the projects you have completed' )


    def __str__(self):
        return self.name_skills

class WorkExpertise(models.Model):
    work_expertise = models.CharField(max_length=255, null=True, verbose_name='Work epertise')
    work_expertise_detail = models.TextField(max_length=255, null=True, verbose_name='Work epertise')
    work_image = models.ImageField(null=True, blank=True, verbose_name="Your work picture: File type: \"jpg or png\": Size 1100x1650 pixels", upload_to='workpicture/')

    def __str__(self):
        return self.work_expertise

class Profession(models.Model):
    add_profession = models.CharField(max_length=255, null=True, verbose_name='Add your Skills')
    def __str__(self):
        return self.add_profession


class YourSkills(models.Model):
    your_skills = models.ManyToManyField(Profession, verbose_name='Plesa choice your Profession')
    your_skills_name = models.CharField(max_length=255, null=True, verbose_name='Skills Name')
    your_knowledge = models.IntegerField( null=True, verbose_name='Skills Present' ) 

    def __str__(self):
        return self.your_skills_name

