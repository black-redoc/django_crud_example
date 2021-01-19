from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
    DetailView,
)
from django.urls import reverse_lazy

from .models import Todo


class ListTodosView(ListView):
    model = Todo


class DetailTodoView(DetailView):
    model = Todo


class CreateTodoView(CreateView):
    model = Todo
    fields = ["title", "description", "priority"]

    def get_success_url(self):
        return reverse_lazy("todos:list")


class UpdateTodoView(UpdateView):
    model = Todo
    fields = ["title", "description", "priority"]

    def get_success_url(self):
        return reverse_lazy("todos:list")


class DeleteTodoView(DeleteView):
    model = Todo

    def get_success_url(self):
        return reverse_lazy("todos:list")