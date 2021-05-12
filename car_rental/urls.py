from django.urls import path
from car_rental import views

urlpatterns = [
    path('data_statistics', views.data_statistics),
]
