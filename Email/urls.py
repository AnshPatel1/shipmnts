from django.contrib import admin
from django.urls import path, include

from Email.router import get_router

urlpatterns = [
    path('auth/', include('Account.urls')),
    path('', include(get_router().urls)),
]
