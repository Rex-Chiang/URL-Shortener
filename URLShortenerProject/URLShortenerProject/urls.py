"""
URLShortenerProject URL Configuration
"""
from URLShortenerApp.views import ShortenURLView, RedirectURLView
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r"api/shorten", ShortenURLView.as_view(), name = "shorten-url" ),
    path(r'<str:shortened_part>/', RedirectURLView.as_view(), name = "redirect"),
]
