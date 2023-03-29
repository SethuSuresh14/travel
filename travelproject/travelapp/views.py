from django.http.response import HttpResponse
from django.shortcuts import render
from  .models import Place
from  .models import detail

# Create your views here.

def home(request):
    obj=Place.objects.all()
    var=detail.objects.all()
    return render(request, "index.html",{'result':obj,'result1':var})
