from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name="home"),
    path('services/',views.services, name="services"),
    path('resume/',views.resume, name="resume"),
    path('projects/',views.projects, name="projects"),
    path('blog/',views.blog, name="blog"),
    path('contact/',views.contact, name="contact"),
    path('test/',views.test, name="test"),


]