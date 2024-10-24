# Caleb Taylor
# CIS 218
# 10/24/2024

from django.contrib.auth import get_user_model

from django.test import TestCase

from django.urls import reverse


# Create your tests here.


class SignUpPageTest(TestCase):
    """Sign Up Page Test"""

    def test_url_exist_at_correct_signupview(self):
        """Test url exist at correct location in the sign up view"""
        response = self.client.get("/accounts/signup/")
        self.assertEqual(response.status_code, 200)

    def test_signup_view_name(self):
        """Test signup view name"""
        response = self.client.get(reverse("signup"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "registration/signup.html")
