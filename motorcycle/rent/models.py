from django.db import models

from motorcycle.accessory.models import Accessory
from motorcycle.motor.models import Motorcycle
from motorcycle.tour.models import Tour


class Rental(models.Model):
    motorcycle = models.ForeignKey(
        Motorcycle,
        on_delete=models.CASCADE,
        related_name='rentals'
    )

    tour = models.ForeignKey(
        Tour,
        on_delete=models.CASCADE,
        related_name='tours',
    )

    pickup_location = models.CharField(
        max_length=100,
        null=False,
        blank=False,
    )

    dropoff_location = models.CharField(
        max_length=100,
        null=False,
        blank=False,
    )

    pickup_date = models.DateField(
        null=False,
        blank=False,
    )

    dropoff_date = models.DateField(
        null=False,
        blank=False,
    )

    accessories = models.ManyToManyField(
        Accessory,
        related_name='rentals',
        blank=True,
    )

    created_date = models.DateField(
        auto_now_add=True,
        blank=True,
    )

    name = models.CharField(
        max_length=155,
        null=False,
        blank=False,
    )

    email = models.EmailField(
        null=False,
        blank=False,
    )

    phone_number = models.CharField(
        max_length=20,
        null=False,
        blank=False,
    )

    message = models.TextField(
        null=False,
        blank=False,
    )

    send_email = models.BooleanField(
        default=False,
    )

    finished = models.BooleanField(
        default=False,
    )


class ContactUs(models.Model):
    name = models.CharField(
        max_length=100,
        null=False,
        blank=False,
    )

    email = models.EmailField(
        null=False,
        blank=False,
    )

    message = models.TextField(
        null=False,
        blank=False,
    )

    date_of_creation = models.DateField(
        auto_now_add=True,
        blank=True,
    )

    send_email = models.BooleanField(
        default=True,
    )

    finished = models.BooleanField(
        default=False,
    )