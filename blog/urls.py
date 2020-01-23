from django.urls import path
from . import views
from django.views.generic.base import TemplateView

urlpatterns = [
    path('', views.index, name='index'),
    path('thread/<int_thread_id>', views.thread, name='thread'),
    path('create/', views.creation_page, name='creation_page'),
    path('create/thread', views.create_thread, name='create_thread'),
    path('thread/<int_thread_id>/comment', views.create_comment, name='create_comment'),
    path('thread/<int_thread_id>/change/ok', views.change_thread, name='change_thread'),
    path('aboutus/', TemplateView.as_view(
        template_name='blog/aboutus.html'), name='info_page'),
]
