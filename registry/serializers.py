from django.db import models
from rest_framework.serializers import ModelSerializer
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
            'last_name', 'email',
            'profile', 'password'
        ]
