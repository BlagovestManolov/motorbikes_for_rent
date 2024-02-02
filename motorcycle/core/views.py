import os.path
from django.http import FileResponse, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import View
from django.views.generic import ListView, CreateView
from django.conf import settings
from motorcycle.about_us.models import AboutUs
from motorcycle.included_in_the_price.models import IncludedInThePrice
from motorcycle.motor.models import Motorcycle
from motorcycle.rent.forms import ContactUsForm
from motorcycle.rent.models import ContactUs


# Create your views here.
class HomePageView(ListView):
    model = Motorcycle
    template_name = 'core/index.html'
    context_object_name = 'motorcycles'

    def get_queryset(self):
        """
        Add images, like related model to the motorcycle
        model!
        """
        return Motorcycle.objects.prefetch_related('images')

    def get_context_data(self, **kwargs):
        """
        Add in the home-page another model!
        """
        context = super().get_context_data(**kwargs)
        context['included_articles'] = IncludedInThePrice.objects.all()
        return context


class ContactPage(CreateView):
    model = ContactUs
    form_class = ContactUsForm
    template_name = 'contacts/contact.html'

    def get_success_url(self):
        return reverse('contact-page')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['our_information'] = AboutUs.objects.first()
        return context


class Custom404View(View):
    def get(self, request, *args, **kwargs):
        return render(request, '404.html', status=404)


def serve_document(request, document_name):
    document_path = os.path.join(settings.STATIC_ROOT, 'document', document_name)
    with open(document_path, 'rb') as document:
        response = HttpResponse(document.read(),
                                content_type='application/pdf')  # Adjust content_type based on your document type
        response['Content-Disposition'] = f'attachment; filename="{document_name}"'
        return response
