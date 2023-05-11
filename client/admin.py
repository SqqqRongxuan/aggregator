from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(passenger)
admin.site.register(booking)
admin.site.register(payment_provider)
admin.site.register(passenger_booking)
admin.site.register(invoice)