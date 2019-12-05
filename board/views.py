# board/views.py

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from .models import Post

class IndexView(generic.ListView):
    model = Post
    paginate_by = 2

class CreateView(generic.CreateView):
    model = Post
    fields = ['title', 'text', 'tags']
    success_url = reverse_lazy('board:index')

class DetailView(generic.DetailView):
    model = Post