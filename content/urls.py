from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('delivery', views.delivery, name='delivery'),
    path('payment', views.payment, name='payment'),
    path('guarantee', views.guarantee, name='guarantee'),
    path('exchange', views.exchange, name='exchange'),
    path('cart-used', views.cart_used, name='cart-used'),
    path('public_offer', views.public_offer, name='public_offer'),
    path('repairs', views.repairs, name='repairs'),

]
