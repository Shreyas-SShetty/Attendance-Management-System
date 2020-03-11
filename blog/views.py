from django.shortcuts import render, get_object_or_404
from .models import Course
from .models import Instructor
from .models import Student


def post_list(request) :
    courses = Course.objects.order_by('name')
    return render(request, 'blog/post_list.html', {'courses' : courses})


def course_detail(request, pk) :
    course = get_object_or_404(Course, pk=pk)
    return render(request, 'blog/course_detail.html', {'course' : course})


def take(request) :
    courses = Course.objects.order_by('name')
    return render(request, 'blog/take.html', {'courses' : courses})

def student_list(request, pk) :
    course = get_object_or_404(Course, pk=pk)
    return render(request, 'blog/student_list.html', {'course' : course})