from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tweets/', include('tweet.urls')),
    path('users/', include('user.urls'))

]
