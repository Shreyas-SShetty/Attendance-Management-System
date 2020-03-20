from django import forms
from .models import Attendance

class PostForm(forms.ModelForm):

    class Meta:
        model = Attendance
        fields = ('student_name', 'course_name', )


