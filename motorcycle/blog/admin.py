from django.contrib import admin
from parler.admin import TranslatableAdmin
from motorcycle.blog.models import Blog, BlogImage, BlogMoreInformation


@admin.register(Blog)
class BlogAdmin(TranslatableAdmin):
    list_display = ('title', 'date_of_creation')
    list_filter = ('translations__date_of_creation',)


@admin.register(BlogImage)
class BlogImageAdmin(admin.ModelAdmin):
    ...


@admin.register(BlogMoreInformation)
class BlogMoreInformationAdmin(TranslatableAdmin):
    list_display = ('blog', 'date_of_creation')
    list_filter = ('translations__date_of_creation',)