# Create your views here.
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django import forms
from quix.pay.gateway.authorizenet import AimGateway
from forms import BillingInformationForm, PersonalInformationForm
from quix.pay.transaction import CreditCard, Address, Customer

def process_payment_form(request):

    if request.POST:
        BillingForm = BillingInformationForm(request.POST)
        PersonalForm = PersonalInformationForm(request.POST)

        if BillingForm.is_valid():
            #TODO (Klein): Do you want to save the CreditCard Object into the database?
            card = CreditCard(
                number = BillingForm.cleaned_data['card_number'],
                month = BillingForm.cleaned_data['expiration_month'],
                year = BillingForm.cleaned_data['expiration_year'],
                first_name = BillingForm.cleaned_data['first_name'],
                last_name = BillingForm.cleaned_data['last_name'],
                code = BillingForm.cleaned_data['security_code']
            )
            #TODO (Klein): Need to glue this Address Object into current site
            address = Address(
                first_name = PersonalForm.cleaned_data['first_name'],
                last_name = PersonalForm.cleaned_data['last_name'],
                company = PersonalForm.cleaned_data['company'],
                address = PersonalForm.cleaned_data['address'],
                city = PersonalForm.cleaned_data['city'],
                state_province = PersonalForm.cleaned_data['state'],
                country = PersonalForm.cleaned_data['country'],
                zipcode = PersonalForm.cleaned_data['zipcode'],
                phone = PersonalForm.cleaned_data['phone'],
            )
            #TODO (Klein): Need to glue this Customer Object into current site
            customer = Customer(
                cust_id = '1234',
                email = 'CUSTOMER EMAIL',
                ip = '255.255.255.255',
                billing_address = address,
                shipping_address = address
            )
            # Creating a gateway model and turning on debugging for testing purposes
            gateway = AimGateway('93T7v7AV6fr5', '3647Q9NA8qVHgdh9')
            gateway.use_test_mode = True
            gateway.use_test_url = True
            
            # use gateway.authorize() for an "authorize only" transaction
            # TODO (Klein): Change "1.00" to whatever the client charges for subscriptions
            response = gateway.sale(1.00, card, customer=customer)
            if response.status == response.APPROVED:
                # this is where you store data from the response object into
                # your models. The response.trans_id would be used to capture,
                # void, or credit the sale later.
                return HttpResponseRedirect('/order_success/')
            else:
                status = "%s - %s" % (response.status_strings[response.status],
                    response.message)
                BillingForm._errors[forms.forms.NON_FIELD_ERRORS] = BillingForm.error_class([status])
    else:
        billinginfo = BillingInformationForm()
        personalinfo = PersonalInformationForm()

    return render_to_response('orderform.html', {'billinginfo': billinginfo, 'personalinfo': personalinfo},
        context_instance=RequestContext(request))