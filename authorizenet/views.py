# Create your views here.
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django import forms
from quix.pay.gateway.authorizenet import AimGateway
from forms import PaymentForm
from quix.pay.transaction import CreditCard, Address, Customer

def process_payment_form(request):

    if request.POST:
        form = PaymentForm(request.POST)
        if form.is_valid():
            card = CreditCard(
                number = form.cleaned_data['card_number'],
                month = form.cleaned_data['expiration_month'],
                year = form.cleaned_data['expiration_year'],
                first_name = form.cleaned_data['first_name'],
                last_name = form.cleaned_data['last_name'],
                code = form.cleaned_data['security_code']
            )
            address = Address(
                first_name = 'Micah',
                last_name = 'Carrick',
                address1 = '1234 Fake St.',
                company = 'Quixotix Software',
                city = 'Portland',
                state_province = 'OR',
                country = 'US',
                postal_code = '97217',
                phone = '(555) 555-5555'
            )
            customer = Customer(
                cust_id = '1234',
                email = 'CUSTOMER EMAIL',
                ip = '255.255.255.255',
                billing_address = address,
                shipping_address = address
            )
            gateway = AimGateway('93T7v7AV6fr5', '3647Q9NA8qVHgdh9')
            gateway.use_test_mode = True
            gateway.use_test_url = True
            # use gateway.authorize() for an "authorize only" transaction
            response = gateway.sale(1.00, card, customer=customer)
            if response.status == response.APPROVED:
                # this is where you store data from the response object into
                # your models. The response.trans_id would be used to capture,
                # void, or credit the sale later.
                return HttpResponseRedirect('/order_success/')
            else:
                status = "%s - %s" % (response.status_strings[response.status],
                    response.message)
                form._errors[forms.forms.NON_FIELD_ERRORS] = form.error_class([status])
    else:
        BillingInformationForm = BillingInformationForm()

    return render_to_response('orderform.html', {'BillingInformationForm': BillingInformationForm,},
        context_instance=RequestContext(request))