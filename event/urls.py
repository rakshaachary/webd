from django.urls import path
from .import views
urlpatterns = [
path('create-student/', views.create_student, name='create_student'),
# Add other URL patterns as needed
]