from django.shortcuts import render

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, status

from . import serializers


class AccountsTokenObtainPairView(TokenObtainPairView):
    serializer_class = serializers.AccountsTokenObtainPairSerializer

class AccountsTokenRefreshView(TokenRefreshView):
    serializer_class = serializers.AccountsTokenRefreshSerializer