from django import forms
from django.forms import ModelForm
from .models import Locals,Tourist,POI_add,POI_rating,hotels,Hotel_add,Hotel_rating,trip_add,bookings


class Localform(ModelForm):
    class Meta:
        model = Locals
        fields = "__all__"

packages = [
    ('premium', 'Premium'),
    ('middle', 'Middle'),
    ('budget', 'Budget'), 
]


class Bookingform(ModelForm):

    prefered_contact = forms.MultipleChoiceField(
        choices=packages, 
        widget=forms.CheckboxSelectMultiple()
    )

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

       
 

        