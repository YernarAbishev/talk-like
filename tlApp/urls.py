from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('log-in/', views.logIn, name='logIn'),
    path('logout/', views.logoutUser, name='logoutUser'),
    path('explore/', views.explore, name='explore'),
    path('user/profile/', views.userProfile, name='userProfile'),
    path('post/create/', views.addPost, name='addPost'),
    path('post/delete/<int:pk>/', views.deletePost, name='deletePost'),
    path('post/details/<int:pk>/', views.postDetails, name='postDetails'),
    path('post/edit/<int:pk>/', views.postEdit, name='postEdit'),
    path('post/update/<int:pk>/', views.postUpdate, name='postUpdate'),
]