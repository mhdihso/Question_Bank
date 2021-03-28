
from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('token/',views.obtain_auth_token),
    path('Question_Bank/',include('Question_Bank.urls')),
]
