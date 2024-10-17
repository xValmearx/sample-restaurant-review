from django.urls import path

from .views import RestaurantView, RestaurantReviewDetailView, RestaurantCreateReview

urlpatterns = [
    path("restaurant/new/", RestaurantCreateReview.as_view(), name="restaurant_review_new"),
    path("restaurant/<int:pk>", RestaurantReviewDetailView.as_view(), name="restaurant_review_details"),
    path("", RestaurantView.as_view(), name="home"),
]
