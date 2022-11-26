from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name ="home"),
    path('<int:year>/<str:month>', views.home, name ="home"),
    path('/tourist',views.tourist, name = "tourist"),
    path('/local',views.local, name = "local"),
    path('/hotel',views.hotel, name = "hotel"),
    path('/search',views.search, name = "search"),
    path('/update',views.update, name = "update"),
    

]
