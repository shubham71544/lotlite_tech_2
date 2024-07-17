from django.shortcuts import get_object_or_404, redirect, render
from career_crm.models import Job
from apply_now_carrer.models import JobApplication


# Create your views here.
def applyNow(request,job_id):
    job = get_object_or_404(Job, id=job_id)
    return render(request, 'apply_now.html', {'job': job})


def applyNowData(request):
    if request.method=="POST":
        # image=request.POST.get("image")
        resume=request.FILES.get('resume')
        first_name=request.POST.get("firstname")
        last_name=request.POST.get("lastname")
        email=request.POST.get("email")
        mobile_phone=request.POST.get("mobilephone")
        experience_years=request.POST.get("experienceyears")
        experience_months=request.POST.get("experiencemonths")
        current_salary=request.POST.get("currentsalary")
        expected_salary=request.POST.get("expectedsalary")
        available_to_join = request.POST.get("available_to_join") == 'on'  # Convert 'on' to True/False
        privacy_policy = request.POST.get("privacy_policy") == 'on' 

        candidates=JobApplication()
        candidates.resume=resume
        candidates.first_name=first_name
        candidates.last_name=last_name
        candidates.email=email
        candidates.mobile_phone=mobile_phone
        candidates.experience_years=experience_years
        candidates.experience_months=experience_months
        candidates.current_salary=current_salary
        candidates.expected_salary=expected_salary
        candidates.available_to_join=available_to_join
        candidates.privacy_policy=privacy_policy
        candidates.save()
        return render(request,'apply_now.html')
    
    from django.shortcuts import get_object_or_404, redirect, render
from career_crm.models import Job
from apply_now_carrer.models import JobApplication
from django.contrib import messages


# Create your views here.
def applyNow(request,job_id):
    job = get_object_or_404(Job, id=job_id)
    return render(request, 'apply_now.html', {'job': job})


def applyNowData(request):
    if request.method=="POST":
        # image=request.POST.get("image")
        resume=request.FILES.get('resume')
        first_name=request.POST.get("firstname")
        last_name=request.POST.get("lastname")
        email=request.POST.get("email")
        mobile_phone=request.POST.get("mobilephone")
        experience_years=request.POST.get("experienceyears")
        experience_months=request.POST.get("experiencemonths")
        current_salary=request.POST.get("currentsalary")
        expected_salary=request.POST.get("expectedsalary")
        available_to_join = request.POST.get("available_to_join") == 'on'  # Convert 'on' to True/False
        privacy_policy = request.POST.get("privacy_policy") == 'on' 

        candidates=JobApplication()
        candidates.resume=resume
        candidates.first_name=first_name
        candidates.last_name=last_name
        candidates.email=email
        candidates.mobile_phone=mobile_phone
        candidates.experience_years=experience_years
        candidates.experience_months=experience_months
        candidates.current_salary=current_salary
        candidates.expected_salary=expected_salary
        candidates.available_to_join=available_to_join
        candidates.privacy_policy=privacy_policy
        candidates.save()
        messages.success(request, 'Your application has been submitted successfully!')
        return redirect(request.META.get('HTTP_REFERER'))  # Redirect to the previous page
    return redirect('/career/')