from django.db import models
from django.urls import reverse

# Create your models here.


class Restaurant(models.Model):
    """Restaurant model"""

    name = models.CharField(max_length=150)

    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)


class Review(models.Model):
    """Model for reviews"""

    restaurant_id = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name="reviews")

    user_id = models.ForeignKey("auth.User", on_delete=models.CASCADE, related_name="reviews")

    body = models.TextField()

    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
