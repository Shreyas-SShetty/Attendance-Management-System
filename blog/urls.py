from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('course/<int:pk>/', views.course_detail, name='course_detail'),
]