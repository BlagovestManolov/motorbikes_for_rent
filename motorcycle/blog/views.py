from django.shortcuts import render
from django.views.generic import ListView, DetailView

from motorcycle.blog.models import Blog


class BlogView(ListView):
    model = Blog
    template_name = 'blog/blog.html'
    context_object_name = 'blogs'


class SpecBlogView(DetailView):
    model = Blog
    template_name = 'blog/spec_blog_page.html'
    context_object_name = 'blog'
