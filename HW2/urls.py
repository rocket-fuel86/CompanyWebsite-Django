"""
Definition of urls for HW2.
"""

from django.urls import path
from django.contrib import admin
from app import views


urlpatterns = [
    path('', views.home, name='home'),
    path('news/', views.news, name='news'),
    path('management/', views.management, name='management'),
    path('contacts/', views.contacts, name='contacts'),
    path('about/', views.about, name='about'),
    path('admin/', admin.site.urls),
]
