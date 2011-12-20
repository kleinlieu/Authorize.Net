from django.db import models

# Create your models here.

####################
#Transaction Model
####################
# This is a model that will store the history of transactions for subscriptions.
# This model will also allow a user to use the Django Admin site to moderate the site
#
#
#
#TODO (Klein): Figure out what user type actually gets privileges to this information

class Transaction(models.Model):
    #TODO (Klein): Replace the underline below when we know how to hook into the current User class
    #Owner = models.ForeignKey(___)

    #Storing the Billing/Contact Address
    company = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)

    #TODO (Klein): What should this display?
    def __unicode__(self):
        pass

    #TODO (Klein): What should this display?
    def __str__(self):
        pass