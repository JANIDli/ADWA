from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('add-post/', views.add_post, name="add-post"),
    path('single-post/<str:pk>/', views.single_post, name="single-post"),
    path('update-post/<str:pk>/', views.update_post, name="update-post"),
    path('delete-post/<str:pk>/', views.delete_post, name="delete-post"),
    path('admin-post/', views.adminpage, name="adminpage"),
]