from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import (UserRegisterationAPIView)
app_name = "users"

urlpatterns = [
    path("user/register/", UserRegisterationAPIView.as_view(), name="user_register"),
]
