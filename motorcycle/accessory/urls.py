from django.urls import path
from motorcycle.accessory import views

urlpatterns = [
    path('<int:pk>/', views.AccessoryView.as_view(), name='spec-accessory-page'),
]