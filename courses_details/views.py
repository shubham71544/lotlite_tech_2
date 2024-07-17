from django.shortcuts import get_object_or_404, redirect, render
from courses_crm.models import Course, TitleHeadingDetail
from .models import Student

# Create your views here.
def course_details(request, id):
    course = get_object_or_404(Course, id=id)
    return render(request, 'courses_details.html', {'course': course})

def enroll_details(request):
    if request.method=="POST":
        name=request.POST.get("name")
        phone_number=request.POST.get("phone_number")
        email=request.POST.get("email")
        courses=request.POST.get("courses")
        message=request.POST.get("message")
        
        student=Student()
        student.name=name
        student.email=email
        student.phone_number=phone_number
        student.courses=courses
        student.message=message
        student.save()
        # return HttpResponse('Data submitted successfully!')
        return redirect("/courses/")
    
    from django.shortcuts import get_object_or_404, redirect, render
from courses_crm.models import Course
from .models import Student
from courses_crm.models import TitleHeading
from django.contrib import messages

# Create your views here.
def course_details(request, id):
   course = get_object_or_404(Course, id=id)
   courses = Course.objects.all()
   headings = TitleHeading.objects.filter(course=course)
   return render(request, 'courses_details.html', {'course': course, 'courses': courses, 'headings': headings})
  

def enroll_details(request):
    if request.method=="POST":
        name=request.POST.get("name")
        phone_number=request.POST.get("phone_number")
        email=request.POST.get("email")
        courses=request.POST.get("courses")
        message=request.POST.get("message")
        
        student=Student()
        student.name=name
        student.email=email
        student.phone_number=phone_number
        student.courses=courses
        student.message=message
        student.save()
        messages.success(request, 'Your application has been submitted successfully!')
        return redirect(request.META.get('HTTP_REFERER'))
    return redirect('/courses/')