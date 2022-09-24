from django.shortcuts import redirect, render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Task
from .forms import TaskCreateForm, TaskUpdateForm


class TodoListView(ListView):
    model = Task
    template_name = 'tasks/templates/todo_list.html'


class TodoCreateView(CreateView):
    model = Task
    template_name = 'tasks/todo_create_form.html'
    form_class = TaskCreateForm
    success_url = '/+'


class TodoUpdateView(UpdateView):
    model = Task
    template_name = 'tasks/todo_update_form.html'
    form_class = TaskUpdateForm
    success_url = '/e'


class TodoDeleteView(DeleteView):
    model = Task
    template_name = 'tasks/todo_delete_form.html'
    success_url = "/-"