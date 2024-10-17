from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Restaurant, Review


class RestaurantView(ListView):
    model = Restaurant

    template_name = "home.html"


class RestaurantReviewDetailView(DetailView):
    model = Restaurant
    template_name = "restaurant_review_details.html"


class RestaurantCreateReview(CreateView):
    model = Review
    template_name = "restaurant_review_new.html"
    fields = ["restaurant", "user", "body", "rating"]
