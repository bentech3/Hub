from django.shortcuts import render

from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = "home.html"

class AboutPageView(TemplateView):
    template_name = "about.html"

class ServicesPageView(TemplateView):
    template_name = "services.html"

class BlogPageView(TemplateView):
    template_name = "blog.html"

class ContactPageView(TemplateView):
    template_name = "contact.html"

class ProgramPageView(TemplateView):
    template_name = "program.html"

