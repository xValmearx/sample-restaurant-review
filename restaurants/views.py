# Caleb Taylor
# CIS 218
# 10/24/2024

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Restaurant, Review

from django.urls import reverse_lazy


class RestaurantView(ListView):
    """Restaurant View"""

    model = Restaurant

    template_name = "home.html"


class RestaurantDetailView(DetailView):
    """Restaurant detail view"""

    model = Restaurant
    template_name = "restaurant_details.html"


class CreateReview(CreateView):
    """Create review view"""

    model = Review
    template_name = "review_new.html"
    fields = ["restaurant", "user", "body", "rating"]


class DetailedReview(DetailView):
    """delete review view"""

    model = Review
    template_name = "review_details.html"


class DeleteReview(DeleteView):
    """delete review view"""

    model = Review

    template_name = "review_delete.html"

    success_url = reverse_lazy("home")


class UpdateReview(UpdateView):
    """Update review view"""

    model = Review

    template_name = "review_update.html"

    fields = ["body", "rating"]
