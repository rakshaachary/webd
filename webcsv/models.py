from django.db import models
class Student(models.Model):
    name = models.CharField(max_length=100)
    event = models.CharField(max_length=100)
    selected = models.BooleanField(default=False)
    def __str__(self):
        return self.name

# Create your models here.
