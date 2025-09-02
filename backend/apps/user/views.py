from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.generics import GenericAPIView, ListAPIView
from rest_framework.response import Response

from backend.apps.user.serializer import UserSerializer

UserModel = get_user_model()

class UserListCreateView(ListAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class UserToAdminView(GenericAPIView):
    def get_queryset(self):
        return UserModel.objects.exclude(id=self.request.user.id)

    def patch(self, *args, **kwargs):
        user = self.get_object()
        if not user.is_staff:
            user.is_staff = True
            user.save()
        serializer = UserSerializer(user)
        return Response(serializer.data, status.HTTP_200_OK)




