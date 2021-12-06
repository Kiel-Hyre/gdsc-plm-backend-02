from django.urls import path

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from . import views

urlpatterns = [
    # path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('token/', views.AccountsTokenObtainPairView.as_view(), name='accounts_obtain_pair'),
    path('token/refresh/', views.AccountsTokenRefreshView.as_view(), name='accounts_token_refresh'),

    path('users/', views.AccountsUsersView.as_view(), name='accounts_users'),
]