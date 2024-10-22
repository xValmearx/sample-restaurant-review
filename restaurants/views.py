from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Restaurant, Review


class RestaurantView(ListView):
    model = Restaurant

    template_name = "home.html"


class RestaurantDetailView(DetailView):
    model = Restaurant
    template_name = "restaurant_details.html"


class CreateReview(CreateView):
    model = Review
    template_name = "review_new.html"
    fields = ["restaurant", "user", "body", "rating"]


class DetailedReview(DeleteView):
    model = Review
    template_name = "review_details.html"
