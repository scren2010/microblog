from profile import Profile

from django.db.models import Q
from django.shortcuts import render
from djoser.conf import User
from rest_framework import status, permissions
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from app.models import Post
from app.serializers import PostSerializer, AddTweetSerializer


class TweetAllView(APIView):
    """ВЫвод всех твитов"""
    permission_classes = [permissions.AllowAny]
    serializer_class = PostSerializer

    def get(self, request):
        tweets = Post.objects.all()
        ser = PostSerializer(tweets, many=True)
        return Response(ser.data)


class UserTweetsView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        tweets = Post.objects.filter(user=request.user)
        ser = PostSerializer(tweets, many=True).data
        return Response(ser)

    def post(self, request):
        ser = AddTweetSerializer(data=request.data)
        if ser.is_valid():
            ser.save(user=request.user)
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class AddLike(APIView):
    """Ставим лайк"""
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        pk = request.data.get("pk")
        post = Post.objects.get(id=pk)
        if request.user in post.user_like.all():
            post.user_like.remove(User.objects.get(id=request.user.id))
            post.like -= 1
        else:
            post.user_like.add(User.objects.get(id=request.user.id))
            post.like += 1
        post.save() 
        return Response(status=201)

class PostIFollow(APIView):
    """Посты мои и мои подписки"""
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        post = Post.objects.filter(
            Q(user_id__in=request.user.profile.get_followers) |
            Q(user_id=request.user.id)
        )
        ser = PostSerializer(post, many=True)
        return Response(ser.data)

