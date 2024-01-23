from django.contrib import admin
from parler.admin import TranslatableAdmin
from motorcycle.faq.models import DepositAndInsurance, Condition


@admin.register(DepositAndInsurance)
class DepositAndInsuranceAdmin(TranslatableAdmin):
    list_display = ('question', 'date_of_creation')
    list_filter = ('translations__date_of_creation',)


@admin.register(Condition)
class ConditionAdmin(TranslatableAdmin):
    list_display = ('question', 'date_of_creation')
    list_filter = ('translations__date_of_creation',)
