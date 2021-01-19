from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class TodosConfig(AppConfig):
    name = "django_crud_example.todos"
    verbose_name = _("Todos")
