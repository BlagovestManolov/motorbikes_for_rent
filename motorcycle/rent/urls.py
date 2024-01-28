from django.urls import path
from motorcycle.rent import views

urlpatterns = [
    path('', views.RentView.as_view(), name='rent-page'),
    path('motorcycle/<slug:slug>/', views.RentalCreateView.as_view(), name='rental-motorcycle-page'),
]
