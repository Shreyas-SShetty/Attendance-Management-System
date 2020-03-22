from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect
from .models import Course
from .forms import PostForm
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .models import Instructor
from .models import Attendance
from .models import Student


def post_list(request) :
    courses = Course.objects.order_by('name')
    return render(request, 'blog/post_list.html', {'courses' : courses})


def course_detail(request, pk) :
    course = get_object_or_404(Course, pk=pk)
    return render(request, 'blog/course_detail.html', {'course' : course})


@login_required
def take(request, pk) :
    teacher = get_object_or_404(User, pk=pk)
    clone_teacher = Instructor.objects.get(name=teacher)
    return render(request, 'blog/take.html', {'clone_teacher' : clone_teacher})


def student_list(request, pk) :
    global course
    course = get_object_or_404(Course, pk=pk)
    teacher = Instructor.objects.get(course_name=course)
    # attendance = Attendance.objects.create(course_name=course, instructor_name=teacher)
    if request.method == "POST" :
        form = PostForm(request.POST, course=course)
        if form.is_valid() :
            form.instance.course_name = course
            form.instance.instructor_name = teacher
            form.instance.published_date = timezone.now()
            form.save()
            return redirect('post_list')
    else :
        form = PostForm(course=course)
    return render(request, 'blog/student_list.html', {'course' : course, 'form' : form})


def register(request) :
    if request.method == "POST" :
        form = UserCreationForm(request.POST)
        if form.is_valid() :
            form.save()
            return redirect('post_list')
    else :
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form' : form})
