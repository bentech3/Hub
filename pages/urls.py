from django.urls import path
from .views import (
    HomePageView, AboutPageView, ServicesPageView,
    BlogPageView, ContactPageView, ProgramPageView
)

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('services/', ServicesPageView.as_view(), name='services'),
    path('blog/', BlogPageView.as_view(), name='blog'),
    path('contact/', ContactPageView.as_view(), name='contact'),
    path('program/', ProgramPageView.as_view(), name='program'),
]
