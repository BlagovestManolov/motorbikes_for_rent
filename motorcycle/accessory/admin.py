from django.contrib import admin
from parler.admin import TranslatableAdmin
from motorcycle.accessory.models import Accessory, AccessoryImage


@admin.register(Accessory)
class AccessoryAdmin(TranslatableAdmin):
    list_display = ('name', 'price_per_day', 'date_of_creation')
    # list_filter = ('price_per_day', 'date_of_creation')
    list_filter = ('translations__price_per_day', 'translations__date_of_creation')


@admin.register(AccessoryImage)
class AccessoryImageAdmin(admin.ModelAdmin):
    list_filter = ('accessory__translations__name',)
