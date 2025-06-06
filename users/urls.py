from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.profile, name='profile'),
]
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('profile/', views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
