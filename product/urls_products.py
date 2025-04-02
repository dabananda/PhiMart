from django.urls import path
from product import views


urlpatterns = [
    path('', views.all_products, name='all_products'),
    path('<int:pk>/', views.product_detail, name='product_detail'),
]
