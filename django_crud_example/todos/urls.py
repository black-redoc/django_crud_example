from django.urls import include, path
from .views import (
    ListTodosView,
    CreateTodoView,
    UpdateTodoView,
    DeleteTodoView,
    DetailTodoView,
)

app_name = "todos"
urlpatterns = [
    path("list/", ListTodosView.as_view(), name="list"),
    path("create/", CreateTodoView.as_view(), name="create"),
    path("update/<int:pk>", UpdateTodoView.as_view(), name="update"),
    path("delete/<int:pk>", DeleteTodoView.as_view(), name="delete"),
    path("detail/<int:pk>", DetailTodoView.as_view(), name="detail"),
]
