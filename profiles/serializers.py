from rest_framework import serializers
from django.contrib.auth.models import User

from app.models import Post

from app.serializers import UserSerializer
from profiles.models import Profile


class ProfileSer(serializers.ModelSerializer):
    """Сериализация профиля"""
    user = UserSerializer()
    follow = UserSerializer(many=True)
    class Meta:
        model = Profile
        fields = ('__all__')


class UserProfileSerialiser(serializers.ModelSerializer):
    """Сериализация пользователя по профилю"""
    profile = ProfileSer()
    class Meta:
        model = User
        fields = ("profile",)


class PostSerializer(serializers.ModelSerializer):
    """Serializer твитов"""
    user = UserProfileSerialiser()
    user_like = UserSerializer(many=True)
    class Meta:
        model = Post
        fields = ("id",
                  "user",
                  "text",
                  "date",
                  "parent",
                  "like",
                  "user_like"
                  )


class EditAvatar(serializers.ModelSerializer):
    """Редактирование автара"""
    class Meta:
        model = Profile
        fields = ("avatar", )


class EditNike(serializers.ModelSerializer):
    """Редактирование ника"""
    class Meta:
        model = Profile
        fields = ("nike", )