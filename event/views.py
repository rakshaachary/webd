from django.shortcuts import render
from .forms import StudentForm
from .models import Project
def create_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
# Create and save the project
            project = Project.objects.create(
                topic=form.cleaned_data['project_topic'],
                languages_used=form.cleaned_data['languages_used'],
                duration=form.cleaned_data['duration']
            )
# Create and save the student
            student = form.save(commit=False)
            student.project = project
            student.save()
            return render(request, 'student_created.html', {'student': student})
    else:
        form = StudentForm()
    return render(request, 'student_form.html', {'form': form})

# Create your views here.
