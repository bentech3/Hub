from django.shortcuts import render
from .models import HomepageContent, AboutInfo, Service, Program

def home(request):
    content = HomepageContent.objects.first()
    return render(request, "home.html", {"content": content})

def about(request):
    about_info = AboutInfo.objects.first()
    return render(request, "about.html", {"about_info": about_info})

def services(request):
    services = Service.objects.all()
    return render(request, "services.html", {"services": services})

def program(request):
    programs = Program.objects.all()
    return render(request, "program.html", {"programs": programs})

def contact(request):
    return render(request, "contact.html")

def blog(request):
    return render(request, "blog.html")
