from django.shortcuts import render, redirect
from django.contrib import messages
from contact_us.models import Contact

def contactUs(request):
    return render(request, "contact.html")

def contactUs_data(request):
    if request.method == "POST":
        name = request.POST.get("name")
        phone_number = request.POST.get("phone_number")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")
        
        contact = Contact(
            name=name,
            email=email,
            phone_number=phone_number,
            subject=subject,
            message=message
        )
        contact.save()
        messages.success(request, 'Data submitted successfully!')
        return redirect('/contact/')  # Ensure the name matches the URL pattern name
    else:
        messages.error(request, 'This endpoint is for data submission.')
        return redirect('/contact/')
