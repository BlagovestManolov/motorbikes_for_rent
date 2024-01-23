from django.urls import path
from motorcycle.tour import views

urlpatterns = [
    path('', views.TourView.as_view(), name='tour-page'),
    path('<slug:slug>/', views.SpecTourView.as_view(), name='spec-tour-page'),
]