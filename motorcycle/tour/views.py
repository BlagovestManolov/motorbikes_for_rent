from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.generic import CreateView
from django.utils.translation import get_language
from motorcycle.rent.forms import ContactUsForm
from motorcycle.rent.models import ContactUs
from motorcycle.tour.models import Tour, TourImage


# Create your views here.
class TourView(CreateView):
    model = ContactUs
    form_class = ContactUsForm
    template_name = 'tour/tour.html'

    def get_success_url(self):
        return reverse('tour-page')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tours'] = Tour.objects.all()
        return context


class SpecTourView(CreateView):
    model = ContactUs
    form_class = ContactUsForm
    template_name = 'tour/spec_tour_rent.html'

    def get_success_url(self):
        return reverse('tour-page')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        language = get_language()
        slug = self.kwargs.get('slug')
        context['current_tour'] = get_object_or_404(Tour, translations__slug=slug, translations__language_code=language)
        return context
