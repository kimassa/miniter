from django.contrib import admin
from django.urls import path
from user.views import UserView

urlpatterns = [
    path('<int:id>', UserView.as_view()),
    path('', UserView.as_view())
]
