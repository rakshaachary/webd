from django.db import models
class Project(models.Model):
    topic = models.CharField(max_length=255)
    languages_used = models.CharField(max_length=255)
    duration = models.IntegerField() # Assuming duration is in days
    def __str__(self):
        return self.topic
class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True,
    blank=True)
    def __str__(self):
        return self.name
# Create your models here.
