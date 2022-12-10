from django import forms
from django.forms import ModelForm
from .models import Locals,Tourist,POI_add,POI_rating,hotels,Hotel_add,Hotel_rating,trip_add,bookings


class Localform(ModelForm):
    class Meta:
        model = Locals
        fields = "__all__"


class ComparisonForm(forms.Form):
    first_hotel = forms.CharField(max_length = 200)
    Second_hotel = forms.CharField(max_length = 200)




class Bookingform(ModelForm):

    class Meta:
        model = bookings
        fields = "__all__"


class POIadd(ModelForm):
    class Meta:
        model = POI_add
        fields = "__all__"


class tripadd(ModelForm):
    class Meta:
        model = trip_add
        fields = "__all__"


class POIrating(ModelForm):
    class Meta:
        model = POI_rating
        fields = "__all__"


class Hoteladd(ModelForm):
    class Meta:
        model = Hotel_add
        fields = "__all__"


class Hotelrating(ModelForm):
    class Meta:
        model = Hotel_rating
        fields = "__all__"


class Touristform(ModelForm):
    class Meta:
        model = Tourist
        fields = "__all__"


class Hotelform(ModelForm):
    class Meta:
        model = hotels
        fields = "__all__"

       
 

        