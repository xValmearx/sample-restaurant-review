from django.views.generic import ListView, DetailView

from .models import Restaurant, Review


class RestaurantView(ListView):
    model = Restaurant

    template_name = "home.html"


class ReviewDetailView(DetailView):
    model = Restaurant
    template_name = "review_details.html"
