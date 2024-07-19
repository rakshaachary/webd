from .models import Student
from django import forms
class StudentForm(forms.ModelForm):
    project_topic = forms.CharField(max_length=255)
    languages_used = forms.CharField(max_length=255)
    duration = forms.IntegerField()
    class Meta:
        model = Student
        fields = ['name', 'email']