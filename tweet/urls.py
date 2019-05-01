from django.contrib import admin
from django.urls import path
from tweet.views import TweetView, TweetAllView

urlpatterns = [
    path('<int:id>', TweetView.as_view()),
    path('', TweetView.as_view()),
    path('all', TweetAllView.as_view()),
    # path('search/', TweetSearchView.as_view())

]
