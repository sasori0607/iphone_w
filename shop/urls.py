from django.contrib import admin
from django.urls import path, include
from . import views



urlpatterns = [
    path('order', views.order, name='order'),
    path('price', views.price, name='price'),
    path('basket_minus', views.basket_minus, name='basket_minus'),
    path('basket_plus', views.basket_plus, name='basket_plus'),
    path('basket', views.basket, name='basket'),
    path('you_basket', views.you_basket.as_view(), name='you_basket'),
    path('basket_counter', views.basket_counter, name='basket_counter'),
    path('<category>/<slug>', views.Shop_detail_page.as_view(), name='shop_detail'),
    path('<slug>', views.Shop_category.as_view(), name='shop_category'),

]