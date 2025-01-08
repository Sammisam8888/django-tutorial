from django.shortcuts import render

# Create your views here.

def allmyfirstapp(request):
    return render(request, 'myfirstapp/all_myfirstapp.html')
