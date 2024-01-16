from django.shortcuts import render
from .models import Category, Product, Contact
# Create your views here.
def index(request):
    category_list = Category.objects.all()
    return render(request, 'main/index.html', context={
        'category_list':category_list
    })

def products(request, id):
    product_filter = Category.objects.filter(pk=id)
    return render(request, 'main/products.html', context={
        'product_filter':product_filter
    })
def products_detail(request, slug):
    one_product = Product.objects.get(slug=slug)
    return render(request, 'main/products_detail.html', context={
        'one_product':one_product
    })

def contact(request):
   if request.method=='POST':
       email = request.POST.get('email')
       phone = request.POST.get('phone')
       subject = request.POST.get('subject')
       message = request.POST.get('message')
       Contact.objects.create(email=email,phone=phone,subject=subject,message=message)
   return render(request, 'main/contact.html', context={
       })

