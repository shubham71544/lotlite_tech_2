from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from courses_crm.models import Course,TitleHeading, TitleHeadingDetail
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# @login_required(login_url='/login/')
# def coursesData(request):
#     course = Course.objects.all()
#     return render(request,"addcourses.html",{'course':course})

def delete_course(request, course_id):
    if request.method == 'POST':
        course = get_object_or_404(Course, id=course_id)
        course.delete()
        messages.success(request, 'Course deleted successfully.')
        return redirect('/courses_crm/')  # Redirect to a list of courses or another page
    else:
        messages.error(request, 'Invalid request method.')
        return redirect('/courses_crm/')  # Handle the case where the request is not POST

def course_form(request):
    if request.method == 'POST':
        image = request.FILES.get('image')
        title = request.POST.get('title')
        description = request.POST.get('desc')
        what_you_learn = request.POST.get('what_you_learn')
        courses_included = request.POST.get('courses_include')
        course_contents = request.POST.get('course_contents')
        detailed_description = request.POST.get('detailed_desc')

        course = Course(
            image=image,
            title=title,
            description=description,
            what_you_learn=what_you_learn,
            courses_included=courses_included,
            course_contents=course_contents,
            detailed_description=detailed_description
        )
        course.save()

        title_headings = request.POST.getlist('title_headings[]')
        title_heading_details = request.POST.getlist('title_heading_details[]')

        for heading, detail in zip(title_headings, title_heading_details):
            title_heading = TitleHeading(course=course, heading=heading)
            title_heading.save()
            title_heading_detail = TitleHeadingDetail(title_heading=title_heading, detail=detail)
            title_heading_detail.save()

        return redirect('/courses_crm/')  # Replace 'some-view' with your desired redirect URL

    return render(request, 'add_course.html')
