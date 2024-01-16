from django.shortcuts import render, redirect
from .models import Product, Cart
# Create your views here.

def index(request):
    product_list = Product.objects.all()
    cart_list=Cart.objects.all()
    return render(request,'main/index.html', context={
        'product_list':product_list,
        'cart_list':cart_list
    })

def add_to_cart(request):
    if request.method == "POST":
        prod_id = request.POST.get('prod_id')
        my_prod = Product.objects.get(pk=prod_id)
        Cart.objects.create(product=my_prod)
        return redirect('index')

def delete_to_cart(request):
    if request.method =='POST':
        prod_id = request.POST.get('prod_id')
        Cart.objects.filter(pk=prod_id).delete()
        return redirect('cart')
    

def cart(request):
    cart_list=Cart.objects.all()
    return render(request, 'main/cart.html', context={
        'cart_list':cart_list
    })