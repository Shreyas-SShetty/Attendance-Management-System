from django.db import models
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
    name = models.CharField(max_length=20, default='')
    course_name = models.ForeignKey(Course, models.SET_NULL, blank=True, null=True)

    def publish(self) :
        self.save()

    def __str__(self) :
        return self.name

class Attendance(models.Model) :
    course_name = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)