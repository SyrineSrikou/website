from django.shortcuts import render
from django.contrib import messages 
from .models import Contact

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        subject = request.POST['subject']
        message = request.POST['message']

        contact = Contact(name=name, email=email,phone=phone, subject=subject, message=message)
        contact.save()
        messages.success(request, 'Your message has been successfully submitted')
    return render(request,'contacts/contact.html', {})
