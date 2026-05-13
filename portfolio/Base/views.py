from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from Base import models
from Base.models import Contact
from django.shortcuts import render, redirect

# Create your views here.
# def home(request):
#     return render(request,'home.html')
def contact(request):

    if request.method == "POST":
        print("POST request")

        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        content = request.POST.get('content', '')
        number = request.POST.get('number', '')

        print(name, email, number, content)

        if not (2 <= len(name) <= 30):
            messages.error(request, "Name must be between 2 and 30 characters")
            return render(request, "home.html")

        if not (5 <= len(email) <= 50):
            messages.error(request, "Invalid email")
            return render(request, "home.html")

        if not (3 <= len(number) <= 13):
            messages.error(request, "Invalid number")
            return render(request, "home.html")

        ins = Contact(
            name=name,
            email=email,
            number=number,
            content=content
        )

        ins.save()

        messages.success(request, "Thank you! Your message has been saved.")

        return redirect('/')

    return render(request, "home.html")