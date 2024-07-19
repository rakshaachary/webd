from django.urls import path
from .views import *
urlpatterns = [
path('',homefun,name='homefunvar'),
path('registration/',formfun,name='formfunvar'),
path('thankyou/',thankfun,name='thankfunvar'),
]