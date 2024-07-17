from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from apply_now_carrer.models import JobApplication
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/login/')
def applynowView(request):
    candidates=JobApplication.objects.all()
    return render(request,"apply_now_crm.html",{'candidates':candidates})

def delete_Candidate(request, item_id):
    if request.method == "POST":
        item = get_object_or_404(JobApplication, id=item_id)
        item.delete()
        messages.success(request, 'Candidate deleted successfully!')
        return redirect("/apply_now_crm/")  # Redirect to the contact list or appropriate page
    return HttpResponse("Method not allowed", status=405)