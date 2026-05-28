from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'price', 'quantity', 'thumbnail']
        labels = {
            'title': "Назва",
            'price': "Ціна",
            'quantity': "Кількість",
            'thumbnail': "Фото",
        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Назва продукту'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '9.99', 'step': '0.01'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '10'}),
            'thumbnail': forms.ClearableFileInput(attrs={'class': 'form-control', 'accept': 'image/*'}),
        }
        help_texts = {
            'thumbnail': "Дозволено: JPG, JPEG, PNG (максимум 5 МБ)",
        }

    def clean_thumbnail(self):
        thumbnail = self.cleaned_data.get('thumbnail')
        if thumbnail and thumbnail.size > 5 * 1024 * 1024:
            raise forms.ValidationError("Фото занадто велике. Максимальний розмір — 5 МБ.")
        return thumbnail
