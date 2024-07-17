from django.shortcuts import render
from courses_crm.models import Course

# Create your views here.
def courses(request):
    courses=Course.objects.all()
    return render(request,"courses.html",{'courses':courses})
