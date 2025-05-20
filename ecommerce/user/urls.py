# urls.py (in your cart app)
from django.urls import path
from . import views

# app_name = 'cart'

urlpatterns = [
       path('products/', views.product_list, name='product_list'),
       path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),


]
