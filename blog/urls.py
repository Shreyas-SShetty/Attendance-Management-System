from django.urls import path
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('course/<int:pk>/', views.course_detail, name='course_detail'),
    path('student_list/<int:pk>/', views.student_list, name='student_list'),
    path('take/<int:pk>/', views.take, name='take'),
    path('register/', views.register, name='register'),
    path('status/', views.status, name='status'),
    path('status/course/<int:pk>/', views.course_stat, name='course_stat'),
    path('status/course/student/<int:pk1>/<int:pk2>/', views.student_stat, name='student_stat')
]
