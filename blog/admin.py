from django.contrib import admin
from .models import Instructor
from .models import Course
from .models import Student
from .models import Attendance

admin.site.register(Course)
admin.site.register(Student)
admin.site.register(Instructor)
admin.site.register(Attendance)