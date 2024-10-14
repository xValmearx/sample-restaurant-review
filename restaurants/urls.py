from django.urls import path

from .views import RestaurantView, ReviewDetailView

urlpatterns = [
    path("restaurant/<int:pk>", ReviewDetailView.as_view(), name="review_details"),
    path("", RestaurantView.as_view(), name="home"),
]
