from django.urls import path, include


urlpatterns = [
    path('products/', include('product.urls_products')),
    path('categories/', include('product.urls_categories')),
]
