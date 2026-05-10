"""
Definition of views.
"""

from django.shortcuts import render
from django.http import Http404
from django.views import View

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