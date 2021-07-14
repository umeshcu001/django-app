from django.shortcuts import render
from .models import Enquiry
import logging

from django.http import HttpResponse

from math import ceil

# Create your views here.
def index(request):
    if request.method=="POST":
        enquiry = Enquiry()
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        message = request.POST.get('message')
        enquiry.name = name
        enquiry.phone = phone
        enquiry.email = email
        enquiry.message = message
        enquiry.save()
        thank = True
        
        return render(request, "allcontact/index.html", {'thank': thank})

    return render(request, "allcontact/index.html")
