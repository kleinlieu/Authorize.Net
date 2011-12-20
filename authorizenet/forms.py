__author__ = 'KleinLieu'

from django import forms

class BillingInformationForm(forms.Form):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    card_number = forms.CharField(max_length=16)
    expiration_month = forms.CharField(max_length=2)
    expiration_year = forms.CharField(max_length=4)
    security_code = forms.CharField(max_length=4)

class PersonalInformationForm(forms.Form):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
