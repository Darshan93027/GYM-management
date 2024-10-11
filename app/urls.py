"""
URL configuration for strenghtbarathlete project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', home, name='index'),
    path('events/', EventListView.as_view(), name='event-list'),
    path('events/<int:pk>/', EventDetailView.as_view(), name='event-detail'),
    path('programs/', ProgramListView.as_view(), name='program-list'),
    path('programs/<int:pk>/', ProgramDetailView.as_view(), name='program-detail'),
    path('contact-us/', ContactUsView.as_view(), name='contact-us'),
    path('about-me/', AboutMeView.as_view(), name='about-me'),
    path('videos/', VideoView.as_view(), name='videos'),
]