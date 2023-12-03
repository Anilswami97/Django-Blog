from django.shortcuts import render, HttpResponse
from .models import Contact
# Views for the Home page.
def home(request):
    return render(request, "home/home.html")

def about(request):
    return render(request, "home/about.html")

def contact(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        contact = request.POST.get("contact")
        email = request.POST.get("email")
        password = request.POST.get("password")
        message = request.POST.get("message")
        contact = Contact(name = name, contact = contact, email = email, password=password, message = message)
        contact.save()
    return render(request, "home/contact.html")