from django.urls import path
from . import views
urlpatterns=[
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('products/<int:id>/', views.products, name='products'),
    path('products_detail/<slug:slug>/', views.products_detail, name='products_detail')
]