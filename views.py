from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.views import View # Для классового представления

# Функциональное представление
def functional_view(request):
    return render(request, 'second_task/function_based_view.html')

# Классовое представление
class ClassBasedView(View):
    def get(self, request):
        return render(request, 'second_task/class_based_view.html')
