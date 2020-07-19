from djoser.conf import User
from rest_framework import serializers

from app.models import Post

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = '__all__'

class AddTweetSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ('text',)

