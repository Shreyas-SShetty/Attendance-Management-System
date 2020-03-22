from django import forms
from .models import Attendance
from .models import Student


class PostForm(forms.ModelForm) :
    class Meta :
        model = Attendance
        fields = ('student_name',)

    def __init__(self, *args, course=None, **kwargs) :
        super().__init__(*args, **kwargs)
        if self.instance.pk and not course :
            course = self.instance.course_name
        if course :
            self.fields['student_name'].queryset = Student.objects.filter(course_name=course)
