from django.urls import path
from . import views

urlpatterns = [
    path('',        views.home_view,   name='home'),
    path('task-3/', views.task_3_view, name='task-3'),
    path('task-4/', views.task_4_view, name='task-4'),
    path('task-5/', views.task_5_view, name='task-5'),
]