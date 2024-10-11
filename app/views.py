from typing import Any
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, FormView, TemplateView
from .models import *
import random
from .form import ContactForm
from django.core.mail import send_mail
from django.conf import settings
from itertools import chain


def home(request):
    context = {}
    context['programs'] = list(chain(Program.objects.filter(name__icontains="group"), Program.objects.all()[0:3]))
    return render(request, 'index.html', context=context)


class EventListView(ListView):
    model = Event
    template_name = 'events.html'  # Template name
    context_object_name = 'events'  # Variable name to access events in the template
    paginate_by = 10 # Number of events per page

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['view_url'] = reverse_lazy('event-list')
        
        return context


class EventDetailView(DetailView):
    model = Event
    template_name = 'event_detail.html'
    context_object_name = 'current_event'

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        all_events = self.model.objects.exclude(pk=self.object.pk)

        if len(all_events)> 2:
            random_events = random.sample(list(all_events), 2)
        else:
            random_events = all_events
        context['event_list'] = random_events
        return context
    

class ProgramListView(ListView):
    model = Program
    template_name = 'programs.html'  # Template name
    context_object_name = 'programs'  # Variable name to access programs in the template
    paginate_by = 10 # Number of program per page

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['view_url'] = reverse_lazy('program-list')
        return context


class ProgramDetailView(DetailView):
    model = Program
    template_name = 'program_detail.html'
    context_object_name = 'current_program' # Variable name to access

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        all_programs = self.model.objects.exclude(pk=self.object.pk)

        if len(all_programs)> 2:
            random_events = random.sample(list(all_programs), 2)
        else:
            random_events = all_programs
        context['program_list'] = random_events
       
        return context


class ContactUsView(FormView):
    template_name = 'contact_us.html'
    form_class = ContactForm
    success_url = reverse_lazy('contact-us')

    def form_valid(self, form):
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        phone_number = form.cleaned_data['phone_number']
        message = form.cleaned_data['message']

        print(name, email, phone_number, message)
        email_subject = 'Inquiry From Calitalks website'
        email_message = f"Name: {name}\nEmail: {email}\nPhone Number: {phone_number}\nMessage: {message}"

        setattr(form, 'is_valid', True)
        send_mail(
            email_subject,
            email_message,
            settings.EMAIL_HOST_USER,
            [settings.INQUIRY_RECEIVER_EMAIL],
            fail_silently=False,
        )

        return self.render_to_response(self.get_context_data(form=form))

    def form_invalid(self, form):
        setattr(form, 'is_valid', False)
        return self.render_to_response(self.get_context_data(form=form))
    

class AboutMeView(TemplateView):
    template_name = 'about_me.html'


class VideoView(ListView):
    model = YoutubeUrls
    template_name = 'video.html' 
    context_object_name = 'videos'  
    paginate_by = 10



from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import Event, Program

class CustomSitemap(Sitemap):
    changefreq = 'daily'
    priority = 0.5

    def items(self):
        # Define the items to include in the sitemap
        return ['index','events', 'programs', 'contact-us', 'about-me', 'videos']

    def location(self, item):
        # Define the location for each item
        if item == 'events':
            return reverse('events')  # Assuming 'events' is the name of your events page URL in urls.py
        elif item == 'programs':
            return reverse('programs')  # Assuming 'programs' is the name of your programs page URL in urls.py
        else:
            return reverse(item)  # Assuming the rest of the items have their corresponding URL names in urls.py

    def location(self, item):
        if item == 'index':
            return reverse('index')
        elif item == 'events':
            return reverse('event-list')
        elif item == 'programs':
            return reverse('program-list')
        elif item == 'contact-us':
            return reverse('contact-us')
        elif item == 'about-me':
            return reverse('about-me')
        elif item == 'videos':
            return reverse('videos')

    def get_object(self, item):
        if item == 'events':
            return Event.objects.all()
        elif item == 'programs':
            return Program.objects.all()
        else:
            return None

    def get_absolute_url(self, obj):
        if isinstance(obj, Event):
            return reverse('event-detail', kwargs={'pk': obj.pk})
        elif isinstance(obj, Program):
            return reverse('program-detail', kwargs={'pk': obj.pk})
        else:
            return None


def robots_txt_view(request):
    robots_txt_content = """
        User-agent: *
            Disallow: /aldarado/
    """

    # Create an HttpResponse with the robots.txt content
    response = HttpResponse(robots_txt_content, content_type='text/plain')
    return response
