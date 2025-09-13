from django.urls import path
from . import views

urlpatterns = [
    path('', views.attendance_list, name='attendance_list'),
    path('add/', views.attendance_create, name='attendance_create'),
    path('edit/<int:pk>/', views.attendance_update, name='attendance_update'),
    path('delete/<int:pk>/', views.attendance_delete, name='attendance_delete'),
]
