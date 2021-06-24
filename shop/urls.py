from django.urls import path
from shop import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<slug:category_slug>', views.home, name='products_by_name'),
    path('<slug:category_slug>/<slug:product_slug>', views.product, name='product_detail'),
]