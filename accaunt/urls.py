from django.urls import path
from django.contrib import admin
from .views import SignUpView


urlpatterns = [
    path('accounts/', SignUpView.as_view(), name='signup'),
]
