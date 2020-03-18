from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from django.conf import settings


class Course(models.Model) :
    name = models.CharField(max_length=20, default='')
    course_code = models.CharField(max_length=10, default='')

    def publish(self) :
        self.save()

    def __str__(self) :
        return self.name


class Student(models.Model) :
    name = models.CharField(max_length=20, default='')
    rollno = models.CharField(max_length=10, unique=True, default='')
    course_name = models.ManyToManyField(Course)
    email_id = models.EmailField(max_length=40, default='')

    def publish(self) :
        self.save()

    def __str__(self) :
        return self.name


class Instructor(models.Model) :
    name = models.OneToOneField(User, on_delete=models.CASCADE)
    course_name = models.ForeignKey(Course, models.SET_NULL, blank=True, null=True)

    def publish(self) :
        self.save()

    def __str__(self) :
        return str(self.name)


class Attendance(models.Model) :
    course_name = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)
    student_name = models.ForeignKey(Student, on_delete=models.SET_NULL, null=True)
    instructor_name = models.ForeignKey(Instructor, on_delete=models.SET_NULL, null=True)
    published_date = models.DateTimeField(blank=True, null=True)

    class Meta :
        verbose_name = "attendance"
