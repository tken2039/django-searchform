# board/views.py

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from .models import Post
from django.db.models import Q

class IndexView(generic.ListView):
    model = Post
    paginate_by = 2

class CreateView(generic.CreateView):
    model = Post
    fields = ['title', 'text', 'tags']
    success_url = reverse_lazy('board:index')

class DetailView(generic.DetailView):
    model = Post

# 追加
class SearchListView(generic.ListView):
    model = Post
    template_name = 'board/search_list.html'
    paginate_by = 1

    def get_queryset(self):
        query = self.request.GET.get('q', None)
        lookups = (
            Q(title__icontains=query) |
            Q(tags__icontains=query)
        )
        if query is not None:
            qs = super().get_queryset().filter(lookups).distinct()
            return qs
        qs = super().get_queryset()
        return qs