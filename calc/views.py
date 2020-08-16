from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return  render(request ,'home.html', {'name' : 'Mercy'});


def add(request): 

    val1 = int(request.POST['num1'])
    val2 = int(request.POST['num2'])

    val3 = val1 + val2

    return render(request , 'result.html',{'result' : val3})   

def added(request):
    
    return render(request , 'base.html')