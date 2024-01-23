from django.contrib import admin
from parler.admin import TranslatableAdmin
from motorcycle.about_us.models import AboutUs


@admin.register(AboutUs)
class AboutUsAdmin(TranslatableAdmin):
    list_display = ['address',]