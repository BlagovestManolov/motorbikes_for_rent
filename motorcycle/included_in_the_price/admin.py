from django.contrib import admin
from parler.admin import TranslatableAdmin
from motorcycle.included_in_the_price.models import IncludedInThePrice


@admin.register(IncludedInThePrice)
class IncludedInThePriceAdmin(TranslatableAdmin):
    list_display = ('name', 'date_of_creation')
    list_filter = ('translations__date_of_creation',)