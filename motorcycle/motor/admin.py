from django.contrib import admin
from parler.admin import TranslatableAdmin
from motorcycle.motor.models import Motorcycle, MotorcycleImage, MotorcycleDeposit, MotorcycleSpecification


@admin.register(Motorcycle)
class MotorcycleAdmin(TranslatableAdmin):
    list_display = ('name', 'date_of_creation')
    list_filter = ('translations__name', 'translations__date_of_creation')


@admin.register(MotorcycleImage)
class MotorcycleImageAdmin(admin.ModelAdmin):
    list_filter = ('motorcycle__translations__name',)


@admin.register(MotorcycleDeposit)
class MotorcycleDepositAdmin(admin.ModelAdmin):
    list_display = ('motorcycle', 'deposit', 'date_of_creation')


@admin.register(MotorcycleSpecification)
class MotorcycleSpecificationAdmin(TranslatableAdmin):
    list_display = ('motorcycle',)
