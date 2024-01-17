from django.shortcuts import render
from django.views.generic import DeleteView
from django.views.generic import CreateView
from django.views.generic import ListView
from django.views.generic import UpdateView

from django.urls import reverse_lazy

from .models import Todo
from .models import UserTodo


class TodoListView(ListView):
    model = Todo
    template_name = 'core/todo_list.html'

class TodoCreateView(CreateView):
    model = Todo
    template_name = 'todo_form.html'
    fields = ['title', 'description', 'date', 'is_finished']

class TodoUpdateView(UpdateView):
    model = Todo
    template_name = 'todo_form.html'
    fields = ['title', 'description', 'date', 'is_finished']

class TodoDeleteView(DeleteView):
    model = Todo
    template_name = 'todo_confirm_delete.html'
    success_url = reverse_lazy('todo_list')
