
from django.http import HttpResponse
from django.views import generic
from .models import Post
from django.views.generic import ListView


class PostView(ListView):
    model = Post
    template_name = 'index.html'
    ordering = ['-created_on']


class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'