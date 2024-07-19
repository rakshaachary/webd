from django.shortcuts import render
from .models import Student
from .utils import generate_csv_response, generate_pdf_response
def student_list(request):
    Student.objects.get_or_create(name="Gaurav", event="Anchoring", selected=True)
    Student.objects.get_or_create(name="Kanti", event="Dance", selected=True)
    Student.objects.get_or_create(name="Shalini", event="Decoration",selected=False)
    students = Student.objects.filter(selected=True)
    return render(request, 'student_list.html', {'students': students})
def generate_csv_view(request):
    queryset = Student.objects.all()
    return generate_csv_response(queryset, 'students_data')
def generate_pdf_view(request):
    queryset = Student.objects.all()
    return generate_pdf_response(queryset, 'students_data')
# Create your views here.
