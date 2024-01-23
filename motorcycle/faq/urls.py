from django.urls import path
from motorcycle.faq import views

urlpatterns = [
    path('', views.FAQView.as_view(), name='faq-page'),
]