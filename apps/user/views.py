from django.contrib.auth import get_user_model
from django.shortcuts import render

from rest_framework.generics import ListAPIView


UserModel = get_user_model()

class UserListCreateView(ListAPIView):
    queryset = UserModel.objects.all()
    serializer_class =
