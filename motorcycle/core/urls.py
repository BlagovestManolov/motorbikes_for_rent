from django.urls import path
from motorcycle.core import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home-page'),
    path('contact/', views.ContactPage.as_view(), name='contact-page'),
    path('static/document/<str:document_name>', views.serve_document, name='serve_document'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
