from django.shortcuts import render
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from app.models import Post
from app.serializers import PostSerializer


class TweetAllView(APIView):
    """ВЫвод всех твитов"""
    permission_classes = [permissions.AllowAny]
    serializer_class = PostSerializer

    def get(self, request):
        tweets = Post.objects.all()
        ser = PostSerializer(tweets, many=True)
        return Response(ser.data)


class UserTweetsView(APIView):

    def get(self,request):
        tweets = Post.objects.filter(user=request.user)
        ser = PostSerializer(tweets, many=True).data
        return Response(ser)