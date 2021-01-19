from django.db import models
from django.utils.translation import gettext_lazy as _


class Todo(models.Model):
    title = models.CharField(_("Titulo"), max_length=20)
    description = models.TextField(_("Descripción"))
    priority = models.CharField(
        _("Prioridad"), max_length=1, choices=(("1", "1"), ("2", "2"), ("3", "3"))
    )
    created_at = models.DateTimeField(_("Fecha Creación"), auto_now_add=True)

    def __str__(self):
        return self.title
