from django.http import HttpResponse
from django.shortcuts import render
from career_crm.models import Job

# Create your views here.
def career(request):
    jobs=Job.objects.all()
    return render(request,"carrer.html",{'jobs':jobs})
