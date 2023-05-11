from django.db import models

# Create your models here.
class passenger(models.Model):
    name = models.CharField(max_length=255)
    gender = models.IntegerField()
    nationality = models.CharField(max_length=64)
    passport = models.CharField(max_length=128)

class booking(models.Model):
    booking_num = models.CharField(max_length=255)
    flight_id = models.IntegerField()
    price = models.FloatField()
    status = models.CharField(max_length=128)

class passenger_booking(models.Model):
    passenger_id = models.ForeignKey(to=passenger,to_field="id",on_delete=models.DO_NOTHING)
    booking_id = models.ForeignKey(to=booking, to_field="id",on_delete=models.DO_NOTHING)

class payment_provider(models.Model):
    provider_name = models.CharField(max_length=255)
    user_firstName = models.CharField(max_length=255)
    user_lastName = models.CharField(max_length=255)
    user_password = models.CharField(max_length=512)

class invoice(models.Model):
    invoice_num = models.CharField(max_length=255)
    booking_id = models.ForeignKey(to=booking, to_field="id",on_delete=models.DO_NOTHING)
    payment_provider_id = models.ForeignKey(to=payment_provider, to_field="id",on_delete=models.DO_NOTHING)
    status = models.CharField(max_length=255)
    data_time = models.DateTimeField()
    stamp = models.CharField(max_length=255)


