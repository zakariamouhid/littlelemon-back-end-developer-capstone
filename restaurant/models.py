from django.db import models
from django.contrib.auth.models import User

class Menu(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.IntegerField()
    def __str__(self):
        return f'{self.title} (${self.price})'

class Booking(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookings')
    name = models.CharField(max_length=255)
    no_of_guests = models.IntegerField()
    booking_date = models.DateTimeField()
    def __str__(self):
        return f'Booking for {self.name} on {self.booking_date.strftime("%Y-%m-%d %H:%M")} for {self.no_of_guests} guest(s)'