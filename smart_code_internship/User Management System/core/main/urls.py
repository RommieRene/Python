from django.urls import path
from .views import (
    HomeListAPIView,
    HomeListCreateAPIView,
    HomeUpdateAPIView,
    HomeDeleteAPIView,
    HomeRetrieveUpdateDestroyAPIView
)



urlpatterns = [
    path('' , HomeListAPIView.as_view()),
    path('add/' , HomeListCreateAPIView.as_view()),
    path('update/<int:pk>/' , HomeUpdateAPIView.as_view()),
    path('delete/<int:pk>/' , HomeDeleteAPIView.as_view()),
    path("papa/<int:pk>/" , HomeRetrieveUpdateDestroyAPIView.as_view())
]
