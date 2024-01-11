from email.policy import default
from random import choices
from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length = 255)
    description = models.TextField()
    price = models.DecimalField(max_digits = 6, decimal_places = 2)
    inventory = models.IntegerField()
    last_update = models.DateTimeField(auto_now_add = True)

class Customer(models.Model):
    MEMBERSHIP_BRONZE = 'B'
    MEMBERSHIP_SILVER = 'S'
    MEMBERSHIP_GOLD = 'G'

    MEMBERSHIP_CHOICES = [
        (MEMBERSHIP_BRONZE, "Bronze"),
        (MEMBERSHIP_SILVER, "Silver"),
        (MEMBERSHIP_GOLD, "Gold")
    ]

    first_name = models.CharField(max_length = 56)
    last_name = models.CharField(max_length = 56)
    email = models.EmailField(unique = True)
    phone = models.CharField(max_length=50)
    birth_date = models.DateField(null = True)
    membership = models.CharField(max_length = 10, choices = MEMBERSHIP_CHOICES, default = MEMBERSHIP_BRONZE)

class Order(models.Model):
    PAYMENT_PENDING = 'P'
    PAYMENT_COMPLETE = 'C'
    PAYMENT_FAILED = 'F'

    PAYMENT_STATUS = [
        (PAYMENT_PENDING, 'Pending'),
        (PAYMENT_COMPLETE, 'Complete'),
        (PAYMENT_FAILED, 'Failed')
    ]

    placed_at = models.DateTimeField(auto_now_add = True)
    payment_status = models.CharField(max_length = 10, choices = PAYMENT_STATUS, default = PAYMENT_PENDING)