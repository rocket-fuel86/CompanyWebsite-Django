from datetime import datetime

from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from django.contrib import messages
from django.views import View
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from app.forms import ProductForm
from app.models import Product
from app.serializers import ProductSerializer


@api_view(['GET', 'POST'])
def product_list(request):
    if request.method == 'GET':
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True, context={'request': request})
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = ProductSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)

    if request.method == 'GET':
        serializer = ProductSerializer(product, context={'request': request})
        return Response(serializer.data)

    if request.method in ('PUT', 'PATCH'):
        partial = request.method == 'PATCH'
        serializer = ProductSerializer(
            product, data=request.data, partial=partial,
            context={'request': request}
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

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