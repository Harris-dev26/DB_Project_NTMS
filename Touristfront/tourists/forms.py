from django import forms
from django.forms import ModelForm
from .models import Locals,hotels,Tourist


class Localform(ModelForm):
    class Meta:
        model = Locals
        fields = "__all__"


class Touristform(ModelForm):
    class Meta:
        
        model = Tourist
        fields = "__all__"


class Hotelform(ModelForm):
    class Meta:
        model = hotels
        fields = "__all__"

       
 

        