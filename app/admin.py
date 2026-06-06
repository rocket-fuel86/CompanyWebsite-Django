from django.contrib import admin
from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'price', 'quantity')
    list_display_links = ('id', 'title')
    list_editable = ('price', 'quantity')
    list_filter = ('quantity',)
    search_fields = ('title',)
    ordering = ('title',)
    list_per_page = 20

    fields = ('title', 'price', 'quantity', 'thumbnail')