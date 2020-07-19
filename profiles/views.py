from django.shortcuts import render
from djoser.conf import User
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.views import APIView

from app.models import Post
from app.serializers import PostSerializer
from profiles.serializers import PostSerializer, ProfileSer, EditAvatar, EditNike
from profiles.models import Profile


# Create your views here.

class ProfileView(APIView):
    """Вывод профиля прользователя"""
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        ser = PostSerializer(Profile.objects.get(user=request.user))
        return Response(ser.data)


class PublicUserInfo(APIView):
    """Публичный профиль пользователя"""
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        obj = Post.objects.filter(user__profile__id=request.GET.get('pk'))
        ser = PostSerializer(obj, many=True).data
        return Response(ser)


class UpdateProfile(APIView):
    """Редактирование профиля"""
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        prof = Profile.objects.get(user=request.user)
        ser = EditAvatar(prof, data=request.data)
        if ser.is_valid():
            if "avatar" in request.FILES:
                ser.save(avatar=request.FILES["avatar"])
                return Response(status=201)
        else:
            return Response(status=400)


class UpdateNike(APIView):
    """Редактирование ника пользователя"""
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        prof = Profile.objects.get(user=request.user)
        ser = EditNike(prof, data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(status=201)
        else:
            return Response(status=400)


class AddFollow(APIView):
    """Подпись на пользователя"""

    def post(self, request):
        pk = request.data.get("pk")
        user = Profile.objects.get(id=pk)
        user.follow.add(User.objects.get(id=request.user.id))
        user.save()
        return Response(status=201)
