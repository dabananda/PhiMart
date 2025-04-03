from django.urls import path
from product import views


urlpatterns = [
    path('', views.ProductList.as_view(), name='all_products'),
    path('<int:pk>/', views.ProductDetail.as_view(), name='product_detail'),
]
