from django.db import models
from rest_framework.serializers import ModelSerializer
from django.contrib.auth.hashers import make_password
from .models import Profile, User


class ProfileSerializer(ModelSerializer):
    class Meta:
        model = Profile
        exclude = ('user', )


class UserSerializer(ModelSerializer):
    profile = ProfileSerializer()

    class Meta:
        model = User
        fields = [
            'id', 'first_name',
            'last_name', 'username', 'email',
            'profile', 'password'
        ]
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validatedData):
        username = validatedData.get('first_name').lower()
        if validatedData.get('last_name', None) is not None:
            username += validatedData.get('last_name')
        user = User.objects.create(
            username=username,
            first_name=validatedData.get('first_name'),
            last_name=validatedData.get('last_name'),
            email=validatedData.get('email'),
            password=make_password(validatedData.get('password'))
        )

        defaults = validatedData['profile']
        defaults['user'] = user
        profile = Profile.objects.update_or_create(
            user=user,
            defaults=defaults
        )
        return user
