from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from django.conf import settings

class Instructor(models.Model) :
    name = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self) :
        return str(self.name)


class Course(models.Model) :
    name = models.CharField(max_length=20, default='')
    course_code = models.CharField(max_length=10, default='')
    instructor_name = models.ForeignKey(Instructor, on_delete=models.SET_NULL, blank=True, null=True)
# If instructor object gets deleted then the instructor option in the course option will be left blank(Can be refilled).

    def __str__(self) :
        return self.name


class Student(models.Model) :
    name = models.CharField(max_length=20, default='')
    rollno = models.CharField(max_length=10, unique=True, default='')
    email_id = models.EmailField(max_length=40, default='')
    course_name = models.ManyToManyField(Course)

    def __str__(self) :
        return self.name


class Attendance(models.Model) :
    course_name = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)
    student_name = models.ManyToManyField(Student)
    instructor_name = models.ForeignKey(Instructor, on_delete=models.SET_NULL, null=True)
    published_date = models.DateTimeField(blank=True, null=True, default=timezone.now)

    class Meta :
        verbose_name = "attendance"
