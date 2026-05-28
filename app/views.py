"""
Definition of views.
"""
from datetime import datetime

from django.shortcuts import render, redirect
from django.http import Http404
from django.contrib import messages
from django.views import View

from app.forms import ProductForm
from app.models import Product


def product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            messages.success(request, "Товар успішно додано!")
            return redirect('product')
    else:
        form = ProductForm()

    products = Product.objects.all()

    return render(request, 'product.html', {
        'form': form,
        'title': 'Відправка резюме',
        'products': products,
        'year': datetime.now().year,
    })

def home(request):
    return render(
        request,
        'index.html',
    )

class NewsView(View):
    def get(self, request):
        return render(request, 'news.html')

    @staticmethod
    def subpath(request, **kwargs):
        raise Http404("Сторінку в розділі Новини не знайдено")

def management(request):
    return render(
        request,
        'management.html',
    )

def contacts(request):
    return render(
        request,
        'contacts.html',
    )

def about(request):
    return render(
        request,
        'about.html',
    )