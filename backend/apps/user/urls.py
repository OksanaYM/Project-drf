from django.urls import path

from backend.apps.user.views import UserListCreateView

urlpatterns = [
    path('', UserListCreateView.as_view(), name='user_list_create'),

]