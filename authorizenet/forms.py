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
    #streetnumber = forms.IntegerField(required=True)
    #streetname = forms.CharField(max_length=50)
    company = forms.CharField(max_length=50)
    address = forms.CharField(max_length=50)
    city = forms.CharField(max_length=50)
    state = forms.CharField(max_length=50)
    country = forms.CharField(max_length=50)
    zipcode = forms.CharField(max_length=50)
    phone = forms.CharField(max_length=50)

#    address = Address(
#                first_name = 'Micah',
#                last_name = 'Carrick',
#                address1 = '1234 Fake St.',
#                company = 'Quixotix Software',
#                city = 'Portland',
#                state_province = 'OR',
#                country = 'US',
#                postal_code = '97217',
#                phone = '(555) 555-5555'
#            )
#            customer = Customer(
#                cust_id = '1234',
#                email = 'CUSTOMER EMAIL',
#                ip = '255.255.255.255',
#                billing_address = address,
#                shipping_address = address
#            )