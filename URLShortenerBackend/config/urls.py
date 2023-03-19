from shortener.views import ShortenView, RedirectView
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r"api/shorten", ShortenView.as_view(), name = "shorten" ),
    path(r'<str:shortened_part>/', RedirectView.as_view(), name = "redirect"),
]
