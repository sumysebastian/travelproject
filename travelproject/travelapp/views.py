from django.shortcuts import render
from . models import place

# Create your views here.
from django.http import HttpResponse

def home(request):
   obj=place.objects.all()
   return render(request,"index.html",{'result':obj})


