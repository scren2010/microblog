from django.urls import path
from profiles import views


urlpatterns = [
    path('', views.ProfileView.as_view()),
    path('public-info/', views.PublicUserInfo.as_view()),
    path('update-ava/', views.UpdateProfile.as_view()),
    path('update-nike/', views.UpdateNike.as_view()),
    path('follow/', views.AddFollow.as_view()),
]
