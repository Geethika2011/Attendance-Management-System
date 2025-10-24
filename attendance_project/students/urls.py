from django.urls import path
from . import views

urlpatterns = [
    path('', views.student_list, name='student_list'),           # View all students
    path('add/', views.student_create, name='student_create'),   # Add a new student
    path('edit/<int:pk>/', views.student_update, name='student_update'),   # Edit student
    path('delete/<int:pk>/', views.student_delete, name='student_delete'), # Delete student
]
