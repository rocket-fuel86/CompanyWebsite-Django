"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render

def home(request):
    return render(
        request,
        'app/index.html',
        {
            'year':datetime.now().year,
        }
    )

def news(request):
    return render(
        request,
        'app/news.html',
        {
            'year':datetime.now().year,
        }
    )

def management(request):
    return render(
        request,
        'app/management.html',
        {
            'year':datetime.now().year,
        }
    )

def contacts(request):
    return render(
        request,
        'app/contacts.html',
        {
            'year':datetime.now().year,
        }
    )

def contacts(request):
    return render(
        request,
        'app/contacts.html',
        {
            'year':datetime.now().year,
        }
    )

def about(request):
    return render(
        request,
        'app/about.html',
        {
            'year':datetime.now().year,
        }
    )
