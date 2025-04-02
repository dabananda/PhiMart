from django.urls import path
from product import views


urlpatterns = [
    path('', views.AllCategories.as_view(), name='all_categories'),
    path('<int:pk>/', views.CategoryDetail.as_view(), name='category_detail'),
]
