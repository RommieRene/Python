from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name='index'),
    path('cart/', views.cart, name='cart'),
    path('add_to_cart/', views.add_to_cart, name='add_to_cart'),
    path('delete_to_cart/', views.delete_to_cart, name='delete_to_cart')

]