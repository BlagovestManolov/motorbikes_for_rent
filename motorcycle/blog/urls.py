from django.urls import path
from motorcycle.blog import views

urlpatterns = [
    path('', views.BlogView.as_view(), name='blog-page'),
    path('<int:pk>/', views.SpecBlogView.as_view(), name='spec-blog-page'),
]
