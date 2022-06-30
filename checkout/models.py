from django.db import models


class Order(models.Model):

    order_number = models.CharField(max_length=32, null=False, editable=False)
    full_name = models.CharField(max_length=50, null=False, editable=False)
    email = models.CharField(max_length=100, null=False, editable=False)
    phone_number = models.CharField(max_length=10, null=False, editable=False)
    country = models.CharField(max_length=40, null=False, editable=False)
    postcode = models.CharField(max_length=10, null=True, editable=True)
    town_or_city = models.CharField(max_length=32, null=False, editable=False)
    street_address = models.CharField(max_length=100, null=False, editable=False)
    county = models.CharField(max_length=80, null=True, editable=True)
    date = models.DateTimeField(auto_now_add=True)
    delivery_cost = models.DecimalField(max_digits=6, decimal_places=2, null=False, default=0)
    order_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    grand_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)