from django.contrib.auth import get_user_model

from rest_framework.generics import ListAPIView

from apps.user.serializer import UserSerializer

UserModel = get_user_model()

class UserListCreateView(ListAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


