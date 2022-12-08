from django.shortcuts import render
import calendar
from calendar import HTMLCalendar
from .forms import Localform,Touristform,Hotelform,POIadd,POIrating,Hoteladd,Hotelrating,tripadd,Bookingform
from .models import Tourist,hotels,Locals,POI_add,POI_rating,Hotel_rating,Hotel_add,trip_add,bookings
from django.http import HttpResponseRedirect
from django.contrib import messages



def update(request):
    return render(request, 'tourists/update.html',{'passo': passo})

def POI_list(request):
    POI_list = POI_rating.objects.all()
    return render(request,'tourists/POI_list.html',{'POI_list':POI_list})

def Hotel_comp(request):
     
    POI_list = Hotel_add.objects.all()
    return render(request,'tourists/Hotel_comp.html',{'POI_list': POI_list})

def Hotel_list(request):
    Hotel_list = Hotel_rating.objects.all()
    return render(request,'tourists/Hotel_list.html',{'Hotel_list':Hotel_list})

def trip_list(request):
    trip_list = trip_add.objects.all()
    return render(request,'tourists/trip_list.html',{'trip_list':trip_list})

def Hotel_add_list(request):
    Hotel_list = Hotel_add.objects.all()
    avail = "Yes"

    for i in Hotel_list:
        if i.a_rooms == 0:
            avail = "No" 

    return render(request,'tourists/Hotel_add_list.html',{'Hotel_list':Hotel_list , 'avail': avail})

def trip_search(request):
    if request.method == "POST":
        searched = request.POST['searched']
        result = trip_add.objects.filter(name__contains= searched)

        return render(request,"tourists/trip_search.html",{ 'searched': searched ,
        'result': result})

    else:

        return render(request,"tourists/trip_search.html",{})

def search(request):
    if request.method == "POST":
        searched = request.POST['searched']
        result = hotels.objects.filter(Tourist_Name__contains= searched)

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

def POI_(request):

    submitted = False 

    if request.method == "POST":

        form = POIadd(request.POST)
        form.save()
        print("error")
        return HttpResponseRedirect('/%2FPOI?submitted=True')

    else:
    
        form = POIadd
        if 'submitted' in request.GET:
            submitted = True
    

    return render(request,"tourists/POI_signup.html",{'form': form , 'submitted': submitted})

def POIrating_(request):

    submitted = False 

    if request.method == "POST":

        form = POIrating(request.POST)
        form.save()
        print("error")
        return HttpResponseRedirect('/%2FPOIrating?submitted=True')

    else:
    
        form = POIrating
        if 'submitted' in request.GET:
            submitted = True
    

    return render(request,"tourists/POI_rating.html",{'form': form , 'submitted': submitted})

def Bookings_(request):

    submitted = False 

    if request.method == "POST":

        form = Bookingform(request.POST)
        form.save()
        return HttpResponseRedirect('/Book?submitted=True')

    else:
    
        form = Bookingform
        if 'submitted' in request.GET:
            submitted = True
    

    return render(request,"tourists/booking.html",{'form': form , 'submitted': submitted})

def Hotel_(request):
    
    submitted = False 

    if request.method == "POST":

        form = Hoteladd(request.POST)
        form.save()
        print("error")
        return HttpResponseRedirect('/%2FHotel?submitted=True')

    else:
    
        form = Hoteladd
        if 'submitted' in request.GET:
            submitted = True
    

    return render(request,"tourists/Hotel_add.html",{'form': form , 'submitted': submitted})

def trip_(request):
        
    submitted = False 

    if request.method == "POST":

        form = tripadd(request.POST)
        form.save()
        print("error")
        return HttpResponseRedirect('/%2Fhome_tourist?submitted=True')

    else:
    
        form = tripadd
        if 'submitted' in request.GET:
            submitted = True
    

    return render(request,"tourists/trip_add.html",{'form': form , 'submitted': submitted})

def Hotelrating_(request):

    submitted = False 

    if request.method == "POST":

        form = Hotelrating(request.POST)
        form.save()
        print("error")
        return HttpResponseRedirect('/%2FHotelrating?submitted=True')

    else:
    
        form = Hotelrating
        if 'submitted' in request.GET:
            submitted = True
    

    return render(request,"tourists/Hotel_rating.html",{'form': form , 'submitted': submitted})

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




 