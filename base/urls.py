from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='Home'),
    path('login/', views.loginPage, name='login'),
    path('register/', views.registerPage, name='register'),
]
