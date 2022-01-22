import pytest
import json
from django.urls import reverse
from URLShortenerApp.views import ShortenURLView, RedirectURLView

pytestmark = pytest.mark.django_db

class TestView:
    def test_ShortenURLView_post_new(self, rf):
        url = "https://www.google.com"
        request = rf.post(reverse("shorten-url"), {"long_url":url})
        response = ShortenURLView.as_view()(request)
        assert response.status_code == 201
        response.render()
        content = json.loads(response.content)
        assert content["long_url"] == url
        assert len(content["short_url"]) == 6
        assert content["request_times"] == 0

    def test_ShortenURLView_post_duplicated(self, rf):
        url = "https://github.com/Rex-Chiang"
        request = rf.post(reverse("shorten-url"), {"long_url":url})
        response = ShortenURLView.as_view()(request)
        assert response.status_code == 303
        response.render()
        content = json.loads(response.content)[0]
        assert content["long_url"] == url
        assert len(content["short_url"]) == 6
        assert content["request_times"] == 0

    def test_ShortenURLView_post_fail(self, rf):
        url = ""
        print(reverse("shorten-url"), {"long_url":url})
        request = rf.post(reverse("shorten-url"), {"long_url":url})
        response = ShortenURLView.as_view()(request)
        assert response.status_code == 400

    def test_RedirectURLView_get_success(self, rf):
        shortened_part = "ICcdEE"
        request = rf.get(reverse("redirect", kwargs = {"shortened_part":shortened_part}))
        response = RedirectURLView.as_view()(request, shortened_part)
        assert response.status_code == 302

    def test_RedirectURLView_get_fail(self, rf):
        shortened_part = "ABCDEF"
        request = rf.get(reverse("redirect", kwargs = {"shortened_part":shortened_part}))
        response = RedirectURLView.as_view()(request, shortened_part)
        assert response.status_code == 404