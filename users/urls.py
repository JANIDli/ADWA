from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_login, name="login"),
    path('register/', views.user_register, name="register"),
    path('user-logout/', views.user_logout, name="user-logout"),
]