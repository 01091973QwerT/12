from lib2to3.fixes.fix_input import context

from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.views import View

def index_view(request):
    return render(request, 'fourth_task/index.html', {'pagename': 'Главная страница'})

class ShopView(View):
    def get(self, request):
        return render(request, 'fourth_task/shop.html', {'games': ['Atomic Heart', 'Cyberpunk 2077']})

class CartView(View):
    def get(self, request):
        return render(request, 'fourth_task/cart.html', {'pagename': 'Корзина'})







