from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from courses_details.models import Student
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='/login/')
def courseContactData(request):
    student=Student.objects.all()
    return render(request,"course_contact.html",{'student':student})



def delete_student(request, student_id):
    if request.method == 'POST':
        student = get_object_or_404(Student, id=student_id)
        student.delete()
        messages.success(request, 'Student deleted successfully.')
        return redirect('course_contact_crm')  # Redirect to a list of courses or another page
    else:
        messages.error(request, 'Invalid request method.')
        return redirect('course_contact_crm')  # Handle the case where the request is not POST