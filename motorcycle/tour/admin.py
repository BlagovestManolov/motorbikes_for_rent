from django.contrib import admin
from parler.admin import TranslatableAdmin
from motorcycle.tour.models import Tour, TourImage, TourMoreInformation


@admin.register(Tour)
class TourAdmin(TranslatableAdmin):
    list_display = ('name', 'price', 'date_of_creation')
    list_filter = ('translations__date_of_creation',)


@admin.register(TourImage)
class TourImageAdmin(admin.ModelAdmin):
    ...


@admin.register(TourMoreInformation)
class TourMoreInformationAdmin(TranslatableAdmin):
    list_display = ('tour',)
