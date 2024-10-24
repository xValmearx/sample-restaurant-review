# Caleb Taylor
# CIS 218
# 10/24/2024
from django.urls import path

from .views import RestaurantView, RestaurantDetailView, CreateReview, DetailedReview, DeleteReview, UpdateReview

urlpatterns = [
    path("review/new/", CreateReview.as_view(), name="review_new"),
    path("review/<int:pk>/", DetailedReview.as_view(), name="review_details"),
    path("restaurant/<int:pk>/", RestaurantDetailView.as_view(), name="restaurant_details"),
    path("review/<int:pk>/edit/", UpdateReview.as_view(), name="review_update"),
    path("review/<int:pk>/delete/", DeleteReview.as_view(), name="review_delete"),
    path("", RestaurantView.as_view(), name="home"),
]
