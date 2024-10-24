from django.urls import path

from . import views ### views ni o'zini chaqirish 


### path yo'l

### url yo'llar
urlpatterns = [
    path('', views.home_page_view, name='home'), 
    path('product_detail/<slug:slug>/', views.product_detail_page_view, name='product-detail'),
    path('products/<slug:slug>/', views.products_page_view, name='products'),
]
