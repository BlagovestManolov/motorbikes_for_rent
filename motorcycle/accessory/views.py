from django.shortcuts import render
from django.views.generic import DetailView
from motorcycle.accessory.models import Accessory
from django.utils.translation import gettext as _


class AccessoryView(DetailView):
    template_name = 'accessory/accessory_page.html'
    model = Accessory
    context_object_name = 'current_accessory'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['all_accessories'] = Accessory.objects.all()
        return context
