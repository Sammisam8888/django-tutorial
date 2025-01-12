from django.shortcuts import render,get_list_or_404,get_object_or_404
from .models import chaiVariety
# Create your views here.

def allmyfirstapp(request):
    chais  = chaiVariety.objects.all()
    return render(request, 'myfirstapp/all_myfirstapp.html', {'chais': chais})

def chai_detail(request, chai_id):
    chai = get_object_or_404(chaiVariety, pk=chai_id)
    return render(request, 'myfirstapp/chai_detail.html', {'chai': chai})