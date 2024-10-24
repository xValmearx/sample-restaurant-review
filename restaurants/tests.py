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
        self.assertEqual(self.review.get_absolute_url(), "/review/1/")

    def test_url_exist_at_correct_location_restaurant_listview(self):
        """Test URL exist at correct location"""

        repsonce = self.client.get("/")
        self.assertEqual(repsonce.status_code, 200)

    def test_url_exist_at_correct_location_restaurant_detailview(self):
        """test URL exist at correct location for the detailview"""

        response = self.client.get("/restaurant/1/")
        self.assertEqual(response.status_code, 200)

    def test_url_exist_at_correct_location_review_detailview(self):
        """test URL exist at correct location for the detailview"""

        response = self.client.get("/review/1/")
        self.assertEqual(response.status_code, 200)

    def test_url_exist_at_correct_location_restaurant_createview(self):
        """test URL exist at correct location for the detailview"""

        response = self.client.get("/review/new/")
        self.assertEqual(response.status_code, 200)

    def test_url_exist_at_correct_location_review_deleteview(self):
        """test URL exist at correct location for the detailview"""

        response = self.client.get("/review/1/delete/")
        self.assertEqual(response.status_code, 200)

    def test_url_exist_at_correct_location_review_update(self):
        """test URL exist at correct location for the detailview"""

        response = self.client.get("/review/1/edit/")
        self.assertEqual(response.status_code, 200)

    def test_restsurant_detailview(self):
        """test restaurant detail page"""
        response = self.client.get("/restaurant/1/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "i like ihop")
        self.assertTemplateUsed(response, "restaurant_details.html")

    def test_review_detailview(self):
        """Test review detail page"""
        response = self.client.get("/review/1/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "ihop")
        self.assertContains(response, "testuser")
        self.assertContains(response, "i like ihop")
        self.assertTemplateUsed(response, "review_details.html")

    def test_review_deleteview(self):
        """test review delete page"""
        response = self.client.get("/review/1/delete/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Are you sure you want to delete")
        self.assertTemplateUsed(response, "review_delete.html")

    def test_review_newview(self):
        """test review new page"""
        response = self.client.get("/review/new/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "create new review")
        self.assertTemplateUsed(response, "review_new.html")

    def test_review_updateview(self):
        """test review update page"""
        response = self.client.get("/review/1/edit/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "are you sure you want to edit this review")
        self.assertTemplateUsed(response, "review_update.html")
