from django.db import models

# Utilities
from marketplace.utils.models import AuditModel


class Product(AuditModel):

    name = models.CharField(
        "Nombre",
        max_length=500
    )

    description = models.TextField(
        "Descripción",
        max_length=10000,
        null=True,
        blank=True
    )

    image = models.ImageField(
        "Imagen",
        upload_to="products/",
        null=True,
        blank=True
    )

    price = models.FloatField(
        "Precio",
        default=0
    )

    purchased = models.BooleanField(
        "Comprado",
        default=False
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
        ordering = ["-created"]
