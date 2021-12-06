from django.shortcuts import render
from django.contrib.auth import get_user_model

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics, status

from . import serializers

User = get_user_model()

class AccountsTokenObtainPairView(TokenObtainPairView):
    serializer_class = serializers.AccountsTokenObtainPairSerializer

class AccountsTokenRefreshView(TokenRefreshView):
    serializer_class = serializers.AccountsTokenRefreshSerializer

class AccountsUsersView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.AccountsUserSerializer
    permission_classes = [IsAuthenticated,]

    def get_queryset(self):
        return self.queryset.exclude(id=self.request.user.pk)