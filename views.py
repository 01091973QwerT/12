from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.views import View

# Функциональное представление для главной страницы
def index_view(request):
    return render(request, 'third_task/index.html')

# Классовое представление для магазина
class ShopView(View):
    def get(self, request):
        shop_items = [
            {'name': 'Игра 1', 'price': 20.99},
            {'name': 'Игра 2', 'price': 15.50},
            {'name': 'Игра 3', 'price': 30.00},
        ]
        return render(request, 'third_task/shop.html', {'shop_items': shop_items})

# Классовое представление для корзины
class CartView(View):
    def get(self, request):
        return render(request, 'third_task/cart.html')
