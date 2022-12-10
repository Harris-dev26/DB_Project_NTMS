from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name ="home"),
    path('/home_hotel', views.home_hotel, name ="home_hotel"),
    path('/home_local', views.home_local, name ="home_local"),
    path('/home_tourist', views.home_tourist, name ="home_tourist"),
    path('/tourist',views.tourist, name = "tourist"),
    path('/local',views.local, name = "local"),
    path('/hotel',views.hotel, name = "hotel"),
    path('/POI',views.POI_, name = "POIadd_"),
    path('/Hotel',views.Hotel_, name = "Hoteladd_"),
    path('/POIrating',views.POIrating_, name = "POIrating_"),
    path('/Hotelrating',views.Hotelrating_, name = "Hotelrating_"),
    path('/hsearch',views.search, name = "search"),
    path('/psearch',views.psearch, name = "psearch"),
    path('/update',views.update, name = "update"),
    path('POI',views.POI_list, name = "list-POI"),
    path('/POI_V',views.POI_view, name = "add-list-POI"),
    path('Hotel',views.Hotel_list, name = "list-Hotel"),
    path('Hotel_add',views.Hotel_add_list, name = "add-list-Hotel"),
    path('Booking_add',views.Booking_view, name = "booking-list-Hotel"),
    path('Hotel_comp',views.Hotel_comp, name = "comp-Hotel"),
    path('Plan',views.trip_, name = "Plan"),
    path('Plan_trip',views.trip_list, name = "list-trip"),
    path('Plan_trip',views.trip_search, name = "trip_search"),
    path('book_search',views.bsearch, name = "b_search"),
    path('Book',views.Bookings_, name = "book"),
     
     
    
     
     
    

]
