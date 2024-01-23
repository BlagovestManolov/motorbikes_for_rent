from django.shortcuts import render
from django.views.generic import ListView

from motorcycle.faq.models import DepositAndInsurance, Condition


# Create your views here.
class FAQView(ListView):
    model = DepositAndInsurance
    template_name = 'faq/faq.html'
    context_object_name = 'deposits'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['conditions'] = Condition.objects.all()
        return context