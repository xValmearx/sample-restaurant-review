from django.views.generic import ListView

from .models import Restaurant


class RestaurantView(ListView):
    model = Restaurant

    template_name = "home.html"
