from django.db import models

# Django
from django.db import models
from django.utils.translation import gettext_lazy as _
import uuid


# Utilities
from marketplace.utils.models import AuditModel


class Buyer(AuditModel):

    uuid = models.CharField(
        'UUID',
        max_length=100,
        unique=True,
    )

    coins = models.IntegerField(
        verbose_name=_("Monedas"),
        default=5000,
    )

    products = models.ManyToManyField(
        "products.Product",
        verbose_name=_("Productos comprados"),
        related_name="buyer",
        blank=True
    )

    def __str__(self):
        return self.uuid

    class Meta:
        verbose_name = _("Comprador")
        verbose_name_plural = _("Compradores")
        ordering = ["uuid"]
