from django.urls import path
from . import views

urlpatterns = [
    path('category/<str:category_name>/', views.GetProductsByCategory.as_view(), name='get_products_by_category'),
    path('create-product/', views.CreateProduct.as_view(), name='create_product'),
    path('list-all-products/', views.ListAllProducts.as_view(), name='list_all_products'),
    path('create-category/', views.CreateCategory.as_view(), name='create_category'),
]   