from django.shortcuts import render
from django.http import HttpResponse

def example_view(request):
    return render(request,'back1.html',{})

# Create your views here.
