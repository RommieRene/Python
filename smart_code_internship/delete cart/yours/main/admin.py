from django.contrib import admin
from .models import Product, Cart
# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id','price','name']
    list_display_links = ['id','name']
    search_fields = ['name','price']

admin.site.register(Cart)