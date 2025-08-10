from rest_framework.generics import ListAPIView
from rest_framework.request import Request

from apps.pizza.serializer import PizzaSerializer


class PizzaListCreateView(ListAPIView):
    serializer_class = PizzaSerializer

    def get_queryset(self):
        request: Request = self.request
        return filter_pizza(request.query_params)

    
