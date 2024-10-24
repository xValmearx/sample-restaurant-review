# Caleb Taylor
# CIS 218
# 10/24/2024

from django.test import TestCase

from django.contrib.auth import get_user_model

from django.urls import reverse

from .models import Restaurant, Review

# Create your tests here.


class ReviewTest(TestCase):
    """Test for the review the"""

    @classmethod
    def setUpTestData(cls):
        """setting up test user"""
        cls.user = get_user_model().objects.create_user(username="testuser", email="test@email.com", password="secret")

        cls.restaurant = Restaurant.objects.create(name="ihop")

        cls.review = Review.objects.create(
            restaurant=cls.restaurant,
            user=cls.user,
            body="i like ihop",
            rating="5",
        )

    def test_user_model(self):
        self.assertEqual(self.review.restaurant.name, "ihop")
        self.assertEqual(self.review.user.username, "testuser")
        self.assertEqual(self.review.body, "i like ihop")
        self.assertEqual(self.review.rating, "5")
        self.assertEqual(self.review.get_absolute_url(), "/review/1")
