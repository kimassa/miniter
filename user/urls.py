from django.contrib import admin
from django.urls import path
from user.views import UserView, UserAllView

urlpatterns = [
    path('<int:id>', UserView.as_view()),
    path('', UserAllView.as_view())
]
