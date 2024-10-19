from django.db import models

# Create your models here.
class Booking(models.Model):
    name = models.CharField(max_length=255)
    guest_number = models.IntegerField()  # Remove the size parameter, Django manages this.
    booking_date = models.DateTimeField()  # Add parentheses to define the field correctly.

    def __str__(self):
        return self.name  # This will help when you print the Booking objects

class Menu(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Use keyword arguments to define this field.
    inventory = models.IntegerField()

    def __str__(self):
        return self.title  # This will help when you print the Menu objects
    
class MenuItem(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.SmallIntegerField()

    def get_item(self):
        return f'{self.title} : {self.price:.2f}'
