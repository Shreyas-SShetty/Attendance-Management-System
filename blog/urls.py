from django.urls import path
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('course/<int:pk>/', views.course_detail, name='course_detail'),
    path('student_list/<int:pk>/', views.student_list, name='student_list'),
    path('take/', views.take, name='take'),
    path('register/', views.register, name='register'),
]