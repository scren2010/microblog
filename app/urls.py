from django.urls import path
from app import views


urlpatterns = [
    path('tweets/', views.TweetAllView.as_view()),
    path('me/', views.UserTweetsView.as_view()),
    path('like/', views.AddLike.as_view()),
    path('follow/', views.PostIFollow.as_view()),
]
