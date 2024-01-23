from django.contrib import admin

from motorcycle.rent.models import Rental, ContactUs


@admin.register(Rental)
class RentalAdmin(admin.ModelAdmin):
    list_display = ('name', 'motorcycle', 'tour', 'pickup_date', 'dropoff_date', 'email', 'created_date', 'finished')
    list_filter = ('created_date', 'motorcycle__translations__name', 'tour__translations__name', 'finished')


@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'date_of_creation', 'finished')
    list_filter = ('date_of_creation', 'finished')