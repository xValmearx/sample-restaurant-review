from django.urls import path

from .views import RestaurantView, RestaurantDetailView, CreateReview, DetailedReview

urlpatterns = [
    path("review/new/", CreateReview.as_view(), name="review_new"),
    path("review/<int:pk>", DetailedReview.as_view(), name="review_details"),
    path("restaurant/<int:pk>", RestaurantDetailView.as_view(), name="restaurant_details"),
    path("", RestaurantView.as_view(), name="home"),
]
