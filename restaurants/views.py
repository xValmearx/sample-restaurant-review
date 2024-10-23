from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Restaurant, Review

from django.urls import reverse_lazy


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


class DetailedReview(DetailView):
    model = Review
    template_name = "review_details.html"


class DeleteReview(DeleteView):
    model = Review

    template_name = "review_delete.html"

    success_url = reverse_lazy("home")


class UpdateReview(UpdateView):
    model = Review

    template_name = "review_update.html"

    fields = ["body", "rating"]
