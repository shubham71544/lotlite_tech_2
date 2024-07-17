from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from career_crm.models import Job
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.decorators import login_required



# Create your views here.
@login_required(login_url='/login/')
def careerData(request):
    job = Job.objects.all()
    return render(request,"Addcareer.html", {'job':job})

def addCareerData(request):
    if request.method=="POST":
        # image=request.POST.get("image")
        title=request.POST.get("title")
        desc=request.POST.get("desc")
        job_type=request.POST.get("job_type")
        location=request.POST.get("location")
        catagory=request.POST.get("catagory")

        Career=Job()
        Career.title=title
        Career.description=desc
        Career.job_type=job_type
        Career.location=location
        Career.category=catagory
    
        Career.save()
        messages.success(request, 'Data submitted successfully.')
        return redirect('career_crm')
    

def delete_career(request, career_id):
    if request.method == 'POST':
        job = get_object_or_404(Job, id=career_id)
        job.delete()
        messages.success(request, 'Career deleted successfully.')
        return redirect('career_crm')  # Redirect to a list of careers or another page
    else:
        messages.error(request, 'Invalid request method.')
        return redirect('career_crm')  # Handle the case where the request is not POST