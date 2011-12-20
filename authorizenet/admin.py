__author__ = 'KleinLieu'

from django.contrib import admin
from authorizenet.models import *

class TransactionAdmin(admin.ModelAdmin):
    pass

admin.site.register(Transaction, TransactionAdmin)