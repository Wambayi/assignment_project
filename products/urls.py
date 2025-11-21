from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_product, name='add_product'),         # Add a product
    path('all/', views.list_products, name='list_products'),     # List all products
    path('<int:pk>/', views.product_detail, name='product_detail'),  # Product details
     path('', views.list_products, name='product_list'), 
]
