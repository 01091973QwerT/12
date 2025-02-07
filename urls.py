from django.urls import path
from . import views

urlpatterns = [
    path('', views.SignUpByDjango.as_view(), name='django_sign_up'),
    path('django_sign_up/', views.SignUpByDjango.as_view(), name='django_sign_up'),
    path('html_sign_up/', views.SignUpByHtml.as_view(), name='html_sign_up'),
]
