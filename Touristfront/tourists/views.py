from django.shortcuts import render
import calendar
from calendar import HTMLCalendar
from .forms import Localform,Touristform,Hotelform
from .models import Tourist,hotels,Locals
from django.http import HttpResponseRedirect


def update(request):
    return render(request, 'tourists/update.html',{'passo': passo})



def search(request):
    if request.method == "POST":
        searched = request.POST['searched']
        result = hotels.objects.filter(name__contains= searched)

        return render(request,"tourists/search.html",{ 'searched': searched ,
        'result': result})

    else:

        return render(request,"tourists/search.html",{})


def tourist(request):
    
    submitted = False 

    if request.method == "POST":

        form = Touristform(request.POST)
        form.save()
        print("error")
        return HttpResponseRedirect('/%2Ftourist?submitted=True')

    else:
    
        form = Touristform
        if 'submitted' in request.GET:
            submitted = True
    

    return render(request,"tourists/tourist_signup.html",{'form': form , 'submitted': submitted})

def local(request):

    submitted = False 

    if request.method == "POST":

        form = Localform(request.POST)
        form.save()
        print("error")
        return HttpResponseRedirect('/%2Flocal?submitted=True')

    else:
    
        form = Localform
        if 'submitted' in request.GET:
            submitted = True
    

    return render(request,"tourists/local_signup.html",{'form': form , 'submitted': submitted})

def hotel(request):
     
    submitted = False 

    if request.method == "POST":

        form = Hotelform(request.POST)
        form.save()
        print("error")
        return HttpResponseRedirect('/%2Fhotel?submitted=True')

    else:
    
        form = Hotelform
        if 'submitted' in request.GET:
            submitted = True
    

    return render(request,"tourists/hotel_signup.html",{'form': form , 'submitted': submitted})


def home(request):
    name = "User"
    return render(request, 'tourists/home.html', { "name" : name,})

def home_hotel(request):
    name = "User"
    return render(request, 'tourists/home_hotel.html', { "name" : name,})

def home_tourist(request):
    name = "User"
    return render(request, 'tourists/home_tourist.html', { "name" : name,})

def home_local(request):
    name = "User"
    return render(request, 'tourists/home_local.html', { "name" : name,})



 