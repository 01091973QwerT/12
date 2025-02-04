from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view, name='index'),
    path('shop/', views.ShopView.as_view(), name='shop'),
    path('cart/', views.CartView.as_view(), name='cart'),
]
