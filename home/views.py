from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact

from django.contrib import messages
# Create your views here.


def index(request):
    context = {
        "variable": "Harry is Great",
        "variable2": "Harry's Tutorial Great"
    }
    return render(request, 'index.html', context)
    # return render(request, 'index.html', context)
    # return HttpResponse("this is Home Page")


def quatoes(request):
    return render(request, './template/quatoes.html')
    # return HttpResponse("this is About Page")


def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        contact = Contact(name=name, email=email,
                          phone=phone, date=datetime.today())
        contact.save()
        messages.success(request, "Form submitted succesfully !")
    return render(request, 'contact.html')
    # return HttpResponse("this is contact Page")
