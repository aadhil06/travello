from django.http import HttpResponse
from django.shortcuts import render
from . models import *
# from .models import nature

# Create your views here.
def fun(request):
    # return HttpResponse("hello world")
    # return render(request,"home.html",{'name':'Addition'})
    # obj=place
    # obj.name="kerala"
    # obj.price=499
    # obj.desc="this is kerala"

    obj = place.objects.all()
    nat = nature.objects.all()


    return render(request,"index.html",{'results':obj,'n':nat})


def addition(request):
    num1=int(request.POST["num1"])
    num2=int(request.POST["num2"])
    num3=num1+num2
    return render(request,"result.html",{"add":num3})

