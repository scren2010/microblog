from django.urls import path
from profiles import views


urlpatterns = [
    path('', views.ProfileView.as_view()),
    path('public-info/', views.PublicUserInfo.as_view()),
]
