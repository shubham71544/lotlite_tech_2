from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from contact_us.models import Contact
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='/login/')
def contactData(request):
    contact=Contact.objects.all()
    return render(request,"contactDatalist.html",{'contact':contact})

def delete_item(request, item_id):
    if request.method == "POST":
        item = get_object_or_404(Contact, id=item_id)
        item.delete()
        messages.success(request, 'Contact deleted successfully!')
        return redirect("/contact_crm/")  # Redirect to the contact list or appropriate page
    return HttpResponse("Method not allowed", status=405)