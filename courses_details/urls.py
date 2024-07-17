
from django.urls import path
from .views import *

urlpatterns = [
    path('course_details/<int:id>/', course_details, name='course_details'),
    path('enroll_Data/', enroll_details),
    
] 
