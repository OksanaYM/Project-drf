from django.urls import path

from apps.pizza.views import PizzaAddPhotoView, PizzaListCreateView, PizzaRetrieveUpdateDestroyView

urlpatterns = [
    path("", PizzaListCreateView.as_view(), name='pizza_list_create'),
    path("/<int:pk>", PizzaRetrieveUpdateDestroyView.as_view()),
    path("/<int:pk>/photos", PizzaAddPhotoView.as_view()),
]