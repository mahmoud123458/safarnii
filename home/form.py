from django import forms

from . models import Booking


class BookForm(forms.ModelForm):
    class Meta:
        model=Booking
        fields=['date','adults','children','total_price']