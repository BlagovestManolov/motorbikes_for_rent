from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.generic import CreateView, ListView
from django.utils.translation import get_language
from motorcycle.accessory.models import Accessory
from motorcycle.motor.models import Motorcycle
from motorcycle.rent.forms import MotorcycleRentForm
from motorcycle.rent.models import Rental


class RentView(ListView):
    model = Motorcycle
    template_name = 'rent/rent.html'
    context_object_name = 'motorcycles'

    def get_queryset(self):
        return Motorcycle.objects.prefetch_related('images', 'deposit', 'specification')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['accessories'] = Accessory.objects.all()
        return context


class RentalCreateView(CreateView):
    model = Rental
    form_class = MotorcycleRentForm
    template_name = 'rent/spec_motor_rent.html'

    def get_success_url(self):
        return reverse('home-page')

    def form_valid(self, form):
        # motorcycle = form.cleaned_data['motorcycle']  # Retrieve the selected motorcycle
        # form.instance.motorcycle = motorcycle

        # response = super().form_valid(form)
        selected_accessories = form.cleaned_data.get('accessory')

        if selected_accessories:
            self.object.accessories.set(selected_accessories)
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['accessories'] = Accessory.objects.all()
        context['motors'] = Motorcycle.objects.all()
        language = get_language()
        slug = self.kwargs.get('slug')

        context['current_motorcycle'] = get_object_or_404(Motorcycle, translations__slug=slug, translations__language_code=language)
        assert isinstance(context, object)
        return context
