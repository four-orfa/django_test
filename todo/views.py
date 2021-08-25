from django.shortcuts import redirect, render
from django.urls.base import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from .models import TodoModel
from django.urls import reverse_lazy

# Create your views here.


class TodoList(ListView):
    template_name = 'list.html'
    model = TodoModel


class TodoDetail(DetailView):
    template_name = "detail.html"
    model = TodoModel


class TodoCreate(CreateView):
    template_name = 'create.html'
    model = TodoModel
    fields = ('title', 'memo', 'priority', 'duedate')
    # Specify reverse'_lazy' because run after data is saved.
    success_url = reverse_lazy('list')
