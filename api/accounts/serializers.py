from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password

from rest_framework import exceptions, serializers
from rest_framework_simplejwt.serializers import (
    TokenObtainPairSerializer,
    TokenRefreshSerializer
)
from rest_framework.exceptions import ValidationError
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken
from rest_framework_simplejwt.authentication import JWTAuthentication

User = get_user_model()


class AccountsTokenObtainPairSerializer(TokenObtainPairSerializer):

    def validate(self, attrs):
        data = super().validate(attrs)
        data['username'] = self.user.username
        data['email'] = self.user.email

        data['groups'] = self.user.groups.values_list('name', flat=True)
        return data


class AccountsTokenRefreshSerializer(TokenRefreshSerializer):

    def validate(self, attrs):
        refresh = RefreshToken(attrs['refresh'])
        # hax
        jwt_object = JWTAuthentication()
        self.user = jwt_object.get_user(refresh.access_token)

        data = {}
        data['access'] = str(refresh.access_token)
        data['refresh'] = str(RefreshToken.for_user(self.user))
        data['username'] = self.user.username
        data['email'] = self.user.email
        data['groups'] = self.user.groups.values_list('name', flat=True)

        return data


class AccountsRegisterSerializer(TokenObtainPairSerializer):
    email = serializers.EmailField()

    def validate(self, attrs):
        data = attrs
        if User.objects.filter(username=data['username']).exists():
            raise ValidationError('Username has already existed.')

        user = User(username=data['username'], email=data['email']) # not commiting
        validate_password(data['password'], user)

        # if success
        user.set_password(data.pop('password'))
        user.save()

        refresh = self.get_token(user)
        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)
        data['username'] = user.username
        data['email'] = user.email
        data['groups'] = user.groups.values_list('name', flat=True)
        return data


class AccountsUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username', 'email',]