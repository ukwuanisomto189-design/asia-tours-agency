from django import forms
from .models import Tour

class TourForm(forms.ModelForm):
    class Meta:
        model = Tour
        fields = ['origin_country', 'destination_country', 'number_of_nights', 'price']