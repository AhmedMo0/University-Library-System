from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.index, name= 'index'),
    path('signUp/', views.AdminSignUpView, name= 'signUp'),
    path('s_signUp/', views.StudentSignUpView, name= 's_signUp'),
    path('login/', views.loginView, name= 'login'),
    path('logout/', views.logoutView, name= 'logout'),
    path('adminProfile/', views.availableBooksView, name= 'adminProfile'),
    path('userProfile/<str:id>', views.userBorrow, name= 'userProfile'),
    path('userProfile/', views.userProfileView, name= 'userProfile'),
    path('delete/<str:id>', views.deleteView, name= 'delete'),

    
    
    
]
