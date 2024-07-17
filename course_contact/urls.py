from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
   path('course_contact_crm/',courseContactData, name="course_contact_crm"),
     path('delete_student/<int:student_id>/',delete_student, name='delete_student'),
]
