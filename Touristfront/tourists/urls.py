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
    path('/search',views.search, name = "search"),
    path('/update',views.update, name = "update"),
    

]