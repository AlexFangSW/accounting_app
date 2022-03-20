from django.urls import path

from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('login', views.Login.as_view(), name='login'),
    path('signUp', views.SignUp.as_view(), name='signUp'),
    path('search', views.Search.as_view(), name='search'),
]