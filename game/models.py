from django.db import models


class FoodTruck(models.Model):
    location_id = models.CharField(primary_key=True, max_length=10)
    applicant = models.CharField(max_length=255)
    facility_type = models.CharField(max_length=128)
    cnn = models.IntegerField()
    location_description = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    block_lot = models.CharField(max_length=10)
    block = models.CharField(max_length=5)
    lot = models.CharField(max_length=5)
    permit = models.CharField(max_length=11)
    status = models.CharField(max_length=16)
    food_items = models.TextField()
    x = models.DecimalField(max_digits=16, decimal_places=2, null=True)  # 5985417.15
    y = models.DecimalField(max_digits=16, decimal_places=3, null=True)  # 2091453.145
    latitude = models.DecimalField(
        max_digits=16, decimal_places=14
    )  # 37.72188970870838
    longitude = models.DecimalField(
        max_digits=16, decimal_places=13
    )  # -122.4925212449949
    schedule = models.URLField(blank=True)
    days_hours = models.CharField(max_length=16, blank=True)
    noisent = models.CharField(max_length=16, blank=True)
    approved = models.DateTimeField(null=True)
    received = models.CharField(max_length=10, blank=True)
    prior_permit = models.CharField(max_length=10, blank=True)
    expiration_date = models.DateTimeField(null=True)
    fire = models.CharField(max_length=32, blank=True)
    police = models.CharField(max_length=32, blank=True)
    supervisor = models.CharField(max_length=32, blank=True)
    zip = models.CharField(max_length=32, blank=True)
    neighborhoods = models.CharField(max_length=32, blank=True)
