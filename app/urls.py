from django.urls import path, re_path
from .views import (
    home, product, management, contacts, about,
    NewsView, product_list, product_detail,
)

urlpatterns = [
    path('', home, name='home'),
    path('news/', NewsView.as_view(), name='news'),
    re_path(r'^news/.+', NewsView.subpath, name='news_subpath'),
    path('management/', management, name='management'),
    path('product/', product, name='product'),
    path('contacts/', contacts, name='contacts'),
    path('about/', about, name='about'),

    path('api/products/', product_list),
    path('api/products/<int:pk>/', product_detail),
]