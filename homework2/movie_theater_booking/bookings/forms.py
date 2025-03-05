from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    # Using HTML5 datetime-local widget for show_time
    show_time = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))
    
    class Meta:
        model = Booking
        fields = ['seat', 'show_time']
