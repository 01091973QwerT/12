from django.shortcuts import render
from django.views import View
from .forms import UserRegister

users = ["user1", "user2", "admin"]

class SignUpByDjango(View):
    def get(self, request):
        info = {}
        form = UserRegister()
        info['form'] = form
        info['users'] = users
        return render(request, 'fifth_task/registration_page.html', {'info': info})

    def post(self, request):
        form = UserRegister(request.POST)
        info = {'users': users}
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']

            if password != repeat_password:
                info['error'] = 'Пароли не совпадают'
            elif age < 18:
                info['error'] = 'Вы должны быть старше 18'
            elif username in users:
                info['error'] = 'Пользователь уже существует'
            else:
                return render(request, 'fifth_task/registration_page.html', {'info': {'users': users, 'message': f'Приветствуем, {username}!' }}) #Изменён вывод сообщения
        else:
            info['error'] = 'Ошибка валидации формы'
            info['form'] = form

        return render(request, 'fifth_task/registration_page.html', {'info': info})


class SignUpByHtml(View):
    def get(self, request):
        info = {}
        info['users'] = users
        return render(request, 'fifth_task/registration_page.html', {'info': info})

    def post(self, request):
        info = {'users': users}
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')
        try:
            age = int(age)
        except ValueError:
            info['error'] = "Некорректный возраст"
            return render(request, 'fifth_task/registration_page.html', {'info': info})


        if password != repeat_password:
            info['error'] = 'Пароли не совпадают'
        elif age < 18:
            info['error'] = 'Вы должны быть старше 18'
        elif username in users:
            info['error'] = 'Пользователь уже существует'
        else:
            return render(request, 'fifth_task/registration_page.html', {'info': {'users': users, 'message': f'Приветствуем, {username}!' }})

        return render(request, 'fifth_task/registration_page.html', {'info': info})
