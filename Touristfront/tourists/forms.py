from django import forms
from django.forms import ModelForm
from .models import Locals,hotels,Tourist,POI_add,POI_rating


class Localform(ModelForm):
    class Meta:
        model = Locals
        fields = "__all__"



class POIadd(ModelForm):
    class Meta:
        model = POI_add
        fields = "__all__"


class POIrating(ModelForm):
    class Meta:
        model = POI_rating
        fields = "__all__"


class Touristform(ModelForm):
    class Meta:
        model = Tourist
        fields = "__all__"


class Hotelform(ModelForm):
    class Meta:
        model = hotels
        fields = "__all__"

       
 

        