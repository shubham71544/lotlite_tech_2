from django.urls import path
from career.views import *
from courses.views import courses

urlpatterns = [
     path("courses/",courses),
]
