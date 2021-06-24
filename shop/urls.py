from django.urls import path
from shop import views

urlpatterns = [
    path('', views.home, name='home'),
    path('product/', views.product, name='product'),
]