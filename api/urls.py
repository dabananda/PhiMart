from django.urls import path, include
from rest_framework_nested import routers
from product.views import ProductViewSet, CategoryViewSet, ReviewViewSet


router = routers.DefaultRouter()
router.register('products', ProductViewSet)
router.register('categories', CategoryViewSet)

product_router = routers.NestedDefaultRouter(
    router, 'products', lookup='product')
product_router.register('reviews', ReviewViewSet, basename='product_review')


urlpatterns = [
    path('', include(router.urls)),
    path('', include(product_router.urls)),
]
