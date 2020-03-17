from django.shortcuts import render, get_object_or_404, redirect
from .models import Course
from .forms import PostForm
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from .models import Instructor
from .models import Student


def post_list(request) :
    courses = Course.objects.order_by('name')
    return render(request, 'blog/post_list.html', {'courses' : courses})


def course_detail(request, pk) :
    course = get_object_or_404(Course, pk=pk)
    return render(request, 'blog/course_detail.html', {'course' : course})

@login_required
def take(request) :
    courses = Course.objects.order_by('name')
    return render(request, 'blog/take.html', {'courses' : courses})


def student_list(request, pk) :
    global course
    if request.method == "POST" :
        form = PostForm(request.POST)
        if form.is_valid() :
            attendance = form.save(commit=False)
            # attendance.author = request.user
            attendance.published_date = timezone.now()
            attendance.save()
            return redirect('take')
    else :
        course = get_object_or_404(Course, pk=pk)
        form = PostForm()
    return render(request, 'blog/student_list.html', {'course' : course, 'form' : form})
