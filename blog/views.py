from django.shortcuts import render
from .models import Course
from .models import Instructor
from .models import Student


def post_list(request) :
    courses = Course.objects.order_by('name')
    return render(request, 'blog/post_list.html', {'courses' : courses})
