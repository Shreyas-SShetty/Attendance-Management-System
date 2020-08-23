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


def status(request) :
    courses = Course.objects.order_by('name')
    return render(request, 'blog/att_status.html', {'courses' : courses})


def course_stat(request, pk) :
    course = get_object_or_404(Course, pk=pk)
    attendances = Attendance.objects.filter(course_name__name=course)
    attendance_count = attendances.count()
    return render(request, 'blog/particular_attd_status.html',
                  {'attendances' : attendances, 'attendance_count' : attendance_count, 'course' : course})


def student_stat(request, pk1, pk2) :
    course__name = get_object_or_404(Course, pk=pk2)
    student__name = get_object_or_404(Student, pk=pk1)
    attendances = Attendance.objects.filter(course_name__name=course__name, student_name__name=student__name)
    classes = Attendance.objects.filter(course_name__name=course__name)
    class_count = ((attendances.count() * 100) / classes.count())
    student_count = attendances.count()
    return render(request, 'blog/particular_student_status.html',
                  {'student_count' : student_count, 'class_count' : class_count})


def course_detail(request, pk) :
    course = get_object_or_404(Course, pk=pk)
    return render(request, 'blog/course_detail.html', {'course' : course})


@login_required
def take(request, pk) :
    user_name = get_object_or_404(User, pk=pk)
    teacher = Instructor.objects.get(name=user_name)
    all_courses = Course.objects.filter(instructor_name=teacher)
    return render(request, 'blog/take.html', {'all_courses' : all_courses})


def student_list(request, pk) :
    global course
    course = get_object_or_404(Course, pk=pk)
    if request.method == "POST" :
        form = PostForm(request.POST, course=course)
        if form.is_valid() :
            form.instance.course_name = course
            form.instance.instructor_name = course.instructor_name
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
