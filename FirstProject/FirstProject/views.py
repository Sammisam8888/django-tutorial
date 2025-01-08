from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("Hello World, Welcome to the World of Sammisam - Home page")
    return render(request, 'website/index.html')

def about(request):
    # return HttpResponse("Hello World, Welcome to the World of Sammisam - About page")
    return render(request, 'about.html')

def contact(request):
    # return HttpResponse("Hello World, Welcome to the World of Sammisam - Contact me samuelpriyatam@gmail.com")
    return render(request, 'contact.html')


