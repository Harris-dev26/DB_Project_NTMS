from django.shortcuts import render
import calendar
from calendar import HTMLCalendar
from .forms import Localform,Touristform,Hotelform,POIadd,POIrating,Hoteladd,Hotelrating,tripadd,Bookingform,ComparisonForm
from .models import Tourist,hotels,Locals,POI_add,POI_rating,Hotel_rating,Hotel_add,trip_add,bookings
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.db import connection



def update(request):
    
    submitted = False 

    if request.method == "POST":

        form = Hoteladd(request.POST)

        if form.is_valid():
            Name = form.cleaned_data.get("Name")
            l = form.cleaned_data.get("Location")
            ar = form.cleaned_data.get("Available rooms")
            d = form.cleaned_data.get("Details")
            p = form.cleaned_data.get("Premium")
            n = form.cleaned_data.get("Normal")
            b = form.cleaned_data.get("Budget")
            
        
        cursor = connection.cursor()
        cursor.execute("UPDATE tourists_hotel_add SET  location = (%s),  a_rooms = (%s), Details = (%s), budget_pack = (%s), normal_pack = (%s), premium_pack = (%s) WHERE  name = (%s)", [l,ar,d,b,n,p,Name])
        return HttpResponseRedirect('/%2Fupdate?submitted=True')

    else:
    
        form = Hoteladd
        if 'submitted' in request.GET:
            submitted = True
    

    return render(request,"tourists/update.html",{'form': form , 'submitted': submitted})

def POI_list(request):
    cursor = connection.cursor()
    query = f'Select Name,Rating,Review,POI_name,location from tourists_poi_rating,tourists_poi_rating_choose_poi,tourists_poi_add where tourists_poi_add.id = tourists_poi_rating_choose_poi.poi_add_id and tourists_poi_rating_choose_poi.poi_rating_id = tourists_poi_rating.id'
    cursor.execute(query)

    return render(request,'tourists/POI_list.html',{'POI_list':cursor})

def POI_view(request):
    cursor = connection.cursor()
    query = f'Select POI_name,location from tourists_poi_add'
    cursor.execute(query)

    return render(request,'tourists/POI_add_list.html',{'POI_list':cursor})

def Booking_view(request):

    cursor = connection.cursor()
    query = f'Select name,sdate,edate,Package from tourists_bookings'
    cursor.execute(query)

    return render(request,'tourists/booking_add_list.html',{'POI_list':cursor})

def Hotel_comp(request):
    
    submitted = False 
    first = ()
    second = ()

    if request.method == "POST":

        form = ComparisonForm(request.POST)
  
        if form.is_valid():
            Name1 = form.cleaned_data.get("first_hotel")
            Name2 = form.cleaned_data.get("Second_hotel")


        
        cursor = connection.cursor()
        cursor.execute("Select * FROM tourists_hotel_add WHERE name = (%s)",[Name1])

        for i in cursor:
            first = i

        cursor.execute("Select * FROM tourists_hotel_add WHERE name = (%s)",[Name2])

        for e in cursor:
            second = e
        
        
        return render(request,'tourists/comp_list.html',{'first': first, 'second':second})

    else:
    
        form = ComparisonForm
        if 'submitted' in request.GET:
            submitted = True
    
    return render(request,'tourists/Hotel_comp.html',{'form': form, 'submitted': submitted})

def Hotel_list(request):
    cursor = connection.cursor()
    query = f'Select tourists_hotel_rating.Name,Rating,Review,tourists_hotel_add.name,location from tourists_hotel_rating,tourists_hotel_rating_choose_hotel,tourists_hotel_add where tourists_hotel_add.id = tourists_hotel_rating_choose_hotel.hotel_add_id and tourists_hotel_rating_choose_hotel.hotel_rating_id = tourists_hotel_rating.id'
    cursor.execute(query)
 
    return render(request,'tourists/Hotel_list.html',{'Hotel_list':cursor})

def trip_list(request):
    cursor = connection.cursor()
    query = f'Select Tourist_Name,Choose_Hotel1,Choose_Hotel2,Choose_POI1,Choose_POI2,Choose_POI3 from tourists_trip_add'
    cursor.execute(query)

    return render(request,'tourists/trip_list.html',{'trip_list': cursor})

def Hotel_add_list(request):

    cursor = connection.cursor()
    query = f'Select name,location,a_rooms,Details,budget_pack,normal_pack,premium_pack from tourists_hotel_add'
    cursor.execute(query)

    
    avail = "Yes"
 

    return render(request,'tourists/Hotel_add_list.html',{'Hotel_list':cursor , 'avail': avail})

def trip_search(request):

    if request.method == "POST":
        searched = request.POST['searched']
        result = trip_add.objects.filter(name__contains= searched)

        return render(request,"tourists/trip_search.html",{ 'searched': searched ,
        'result': result})

    else:

        return render(request,"tourists/trip_search.html",{})

def bsearch(request):
    if request.method == "POST":
        searched = request.POST['searched']

        cursor = connection.cursor()
        cursor.execute("Select * FROM tourists_bookings WHERE name = (%s)",[searched])


        return render(request,"tourists/bsearch.html",{ 'searched': searched ,
        'result': cursor})

    else:

        return render(request,"tourists/bsearch.html",{})
        
def search(request):
    if request.method == "POST":
        searched = request.POST['searched']

        cursor = connection.cursor()
        cursor.execute("Select * FROM tourists_hotel_add WHERE name = (%s)",[searched])


        return render(request,"tourists/search.html",{ 'searched': searched ,
        'result': cursor})

    else:

        return render(request,"tourists/search.html",{})

def psearch(request):
    if request.method == "POST":
        searched = request.POST['searched']

        cursor = connection.cursor()
        cursor.execute("Select * FROM tourists_POI_add WHERE POI_name = (%s)",[searched])


        return render(request,"tourists/psearch.html",{ 'searched': searched ,
        'result': cursor})

    else:

        return render(request,"tourists/psearch.html",{})

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

        if form.is_valid():
            Name = form.cleaned_data.get("POI_name")
            location = form.cleaned_data.get("location")

        cursor = connection.cursor()
        cursor.execute("INSERT INTO tourists_poi_add (POI_name,location) VALUES (%s,%s)",[Name,location])
        return HttpResponseRedirect('/%2FPOI?submitted=True')

    else:
    
        form = POIadd
        if 'submitted' in request.GET:
            submitted = True
    
    return render(request,"tourists/POI_signup.html",{'form': form , 'submitted': submitted})

def POIrating_(request):

    submitted = False 

    firstname=''
    lastname=''
    emailvalue=''

    if request.method == "POST":

        form = POIrating(request.POST)

        if form.is_valid():
            Name = form.cleaned_data.get("Name")
            Rating = form.cleaned_data.get("Rating")
            Review = form.cleaned_data.get("Review")
            POI = form.cleaned_data.get("Choose_POI")

        print(POI[0])
        
        add_id = 0
        rating_id = 0

        cursor = connection.cursor()
        cursor.execute("INSERT INTO tourists_poi_rating (Name,Rating,Review) VALUES (%s,%s,%s)",[Name,Rating,Review])
        cursor.execute("Select id FROM tourists_poi_add WHERE POI_name = (%s)",[POI[0]])

        for i in cursor:
            add_id = i[0]

        cursor.execute("SELECT max(id) FROM tourist_front.tourists_poi_rating")

        for c in cursor:
            
            rating_id = c
        
        cursor.execute("INSERT INTO tourists_poi_rating_choose_poi (poi_rating_id,poi_add_id) VALUES (%s,%s)",[rating_id,add_id])
        
         
          
        return HttpResponseRedirect('/%2FPOIrating?submitted=True')

    else:
    
        form = POIrating
        if 'submitted' in request.GET:
            submitted = True
    

    return render(request,"tourists/POI_rating.html",{'form': form , 'submitted': submitted})

def Hotel_(request):
    
    submitted = False 

    if request.method == "POST":

        form = Hoteladd(request.POST)
       
        if form.is_valid():
            Name = form.cleaned_data.get("name")
            location = form.cleaned_data.get("location")
            arooms = form.cleaned_data.get("a_rooms")
            details = form.cleaned_data.get("Details")
            bpack = form.cleaned_data.get("budget_pack")
            npack = form.cleaned_data.get("normal_pack")
            ppack = form.cleaned_data.get("premium_pack")

        cursor = connection.cursor()
        cursor.execute("INSERT INTO tourists_hotel_add (name,location,a_rooms,Details,budget_pack,normal_pack,premium_pack) VALUES (%s,%s,%s,%s,%s,%s,%s)",[Name,location,arooms,details,bpack,npack,ppack])
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

        if form.is_valid():
            Name = form.cleaned_data.get("Tourist_Name")
            c1 = form.cleaned_data.get("Choose_Hotel1")
            c2 = form.cleaned_data.get("Choose_Hotel2")
            p1 = form.cleaned_data.get("Choose_POI1")
            p2 = form.cleaned_data.get("Choose_POI2")
            p3 = form.cleaned_data.get("Choose_POI3")
        
        
        cursor = connection.cursor()
        cursor.execute("INSERT INTO tourists_trip_add (Tourist_Name,Choose_Hotel1,Choose_Hotel2,Choose_POI1,Choose_POI2,Choose_POI3) VALUES (%s,%s,%s,%s,%s,%s)",[Name,c1,c2,p1,p2,p3])
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
        
        if form.is_valid():
            Name = form.cleaned_data.get("Name")
            Rating = form.cleaned_data.get("Rating")
            Review = form.cleaned_data.get("Review")
            hotel = form.cleaned_data.get("Choose_Hotel")

        print(hotel[0])
        
        add_id = 0
        rating_id = 0

        cursor = connection.cursor()
        cursor.execute("INSERT INTO tourists_hotel_rating (Name,Rating,Review) VALUES (%s,%s,%s)",[Name,Rating,Review])
        cursor.execute("Select id FROM tourists_hotel_add WHERE name = (%s)",[hotel[0]])

        for i in cursor:
            add_id = i[0]

        cursor.execute("SELECT max(id) FROM tourist_front.tourists_hotel_rating")

        for c in cursor:
            
            rating_id = c
        
        cursor.execute("INSERT INTO tourists_hotel_rating_choose_hotel (hotel_rating_id,hotel_add_id) VALUES (%s,%s)",[rating_id,add_id])
        
        return HttpResponseRedirect('/%2FHotelrating?submitted=True')

    else:
    
        form = Hotelrating
        if 'submitted' in request.GET:
            submitted = True
    

    return render(request,"tourists/Hotel_rating.html",{'form': form , 'submitted': submitted})

def Bookings_(request):

    submitted = False 

    if request.method == "POST":

        form = Bookingform(request.POST)
        
        if form.is_valid():
            Name = form.cleaned_data.get("name")
            Rating = form.cleaned_data.get("sdate")
            Review = form.cleaned_data.get("edate")
            pack = form.cleaned_data.get("Package")
            hotel = form.cleaned_data.get("Choose_Hotel")

        print(hotel[0])
        
        add_id = 0
        rating_id = 0

        cursor = connection.cursor()
        cursor.execute("INSERT INTO tourists_bookings (name,sdate,edate,Package) VALUES (%s,%s,%s,%s)",[Name,Rating,Review,pack])
        cursor.execute("Select id FROM tourists_hotel_add WHERE name = (%s)",[hotel[0]])

        for i in cursor:
            add_id = i[0]

        cursor.execute("SELECT max(id) FROM tourists_bookings")

        for c in cursor:
            
            rating_id = c
        
        cursor.execute("INSERT INTO tourists_bookings_choose_hotel (bookings_id,hotel_add_id) VALUES (%s,%s)",[rating_id,add_id])


        return HttpResponseRedirect('/Book?submitted=True')

    else:
    
        form = Bookingform
        if 'submitted' in request.GET:
            submitted = True
    

    return render(request,"tourists/booking.html",{'form': form , 'submitted': submitted})

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




 