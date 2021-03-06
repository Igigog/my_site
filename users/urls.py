from django.urls import path
from django.contrib.auth import views as auth_views


app_name = 'users'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(
        template_name='users/login.html'), name='login'),
    path('register/', auth_views.TemplateView.as_view(
        template_name='users/register.html'), name='register'),
]
