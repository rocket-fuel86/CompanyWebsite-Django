import os
from django.db import models
from django.core.validators import MinLengthValidator, MinValueValidator


def thumbnail_upload_path(instance, filename):
    ext = os.path.splitext(filename)[1].lower()
    new_name = f"thumbnail_{filename}{ext}"
    return f'thumbnails/{new_name}'


class Product(models.Model):
    title = models.CharField("Назва", max_length=150, validators=[MinLengthValidator(3)])
    price = models.DecimalField("Ціна", max_digits=10, decimal_places=2)
    quantity = models.IntegerField("Кількість", validators=[MinValueValidator(0)])

    thumbnail = models.ImageField("Фото", upload_to=thumbnail_upload_path, blank=True, null=True)

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукти"
        ordering = ['title']

    def __str__(self):
        return f"{self.title} — {self.price}, {self.quantity}"