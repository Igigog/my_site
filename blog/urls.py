from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('thread/<int_thread_id>', views.thread, name='thread'),
    path('create/', views.creation_page, name='creation_page'),
    path('create/thread', views.create_thread, name='create_thread'),
    path('thread/<int_thread_id>/comment', views.create_comment, name='create_comment'),
    path('thread/<int_thread_id>/change/ok', views.change_thread, name='change_thread'),
    path('login/', views.login_page, name='login_page'),
    path('register/', views.register_page, name='register_page'),
    path('register/new', views.register, name='register'),
    path('aboutus/', views.info_page, name='info_page'),
    path('login/new', views.login, name='login'),
    path('register/new', views.register, name='register'),
]