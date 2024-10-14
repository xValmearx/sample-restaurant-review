from django.db import models
from django.urls import reverse

# Create your models here.

# super user: user = caleb,pass= password, email = calebs.phone2017@gmail.com


class Restaurant(models.Model):
    """Restaurant model"""

    name = models.CharField(max_length=150)

    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name[:50]


class Review(models.Model):
    """Model for reviews"""

    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name="reviews")

    user = models.ForeignKey("auth.User", on_delete=models.CASCADE, related_name="reviews")

    body = models.TextField()

    ratings_choices = (
        ("five", "5"),
        ("four", "4"),
        ("three", "3"),
        ("two", "2"),
        ("one", "1"),
    )

    rating = models.CharField(max_length=6, choices=ratings_choices, default="five")

    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.body[:50]
