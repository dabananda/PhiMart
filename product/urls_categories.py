from django.urls import path
from product import views


urlpatterns = [
    path('', views.all_categories, name='all_categories'),
    path('<int:pk>/', views.category_detail, name='category_detail'),
]
