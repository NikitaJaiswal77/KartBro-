# views.py
from django.shortcuts import get_object_or_404, redirect,render
from django.contrib import messages

from .models import Product
from .models import Cart
def product_list(request):
    products = Product.objects.all()
    return render(request, 'user/home.html', {'products': products})
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if request.user.is_authenticated:
        cart_item, created = Cart.objects.get_or_create(user=request.user, product=product)
        if not created:
            cart_item.quantity += 1
            cart_item.save()
        # Add success message
        messages.success(request, f'{product.name} has been added to your cart!')
    else:
        # Optional: handle guest users using session
        cart = request.session.get('cart', {})
        cart[str(product_id)] = cart.get(str(product_id), 0) + 1
        request.session['cart'] = cart
        # Add success message for guest user
        messages.success(request, f'{product.name} has been added to your cart!')
# 
    return redirect('product_list')  # Redirect to the product list or cart page