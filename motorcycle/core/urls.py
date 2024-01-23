from django.urls import path
from motorcycle.core import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home-page'),
    path('contact/', views.ContactPage.as_view(), name='contact-page'),
]