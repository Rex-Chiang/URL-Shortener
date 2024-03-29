import pytest
import json
from django.urls import reverse
from shortener.models import Record
from shortener.views import ShortenView, RedirectView

pytestmark = pytest.mark.django_db

class TestView:
    def test_shorten_post_new(self, rf):
        url = "https://www.google.com"
        request = rf.post(reverse("shorten-url"), {"long_url":url})
        response = ShortenView.as_view()(request)

        assert response.status_code == 201

        response.render()
        content = json.loads(response.content)

        assert content["long_url"] == url
        assert len(content["short_url"]) == 6
        assert content["request_times"] == 0

    def test_shorten_post_duplicated(self, rf):
        url = "https://github.com/Rex-Chiang"
        request = rf.post(reverse("shorten-url"), {"long_url":url})
        response = ShortenView.as_view()(request)

        assert response.status_code == 303

        response.render()
        content = json.loads(response.content)

        assert content["long_url"] == url
        assert len(content["short_url"]) == 6
        assert content["request_times"] == 0

    def test_shorten_post_fail(self, rf):
        url = ""
        print(reverse("shorten-url"), {"long_url":url})
        request = rf.post(reverse("shorten-url"), {"long_url":url})
        response = ShortenView.as_view()(request)

        assert response.status_code == 400

    def test_redirect_get_success(self, rf):
        shortened_part = "UkXhNv"
        request = rf.get(reverse("redirect", kwargs={"shortened_part":shortened_part}))
        response = RedirectView.as_view()(request, shortened_part)

        assert response.status_code == 302

    def test_redirect_get_fail(self, rf):
        shortened_part = "ABCDEF"
        request = rf.get(reverse("redirect", kwargs={"shortened_part":shortened_part}))
        response = RedirectView.as_view()(request, shortened_part)

        assert response.status_code == 404

    def test_redirect_get_consecutive(self, rf):
        shortened_part = "UkXhNv"
        for i in range(3):
            request = rf.get(reverse("redirect", kwargs={"shortened_part":shortened_part}))
            RedirectView.as_view()(request, shortened_part)

        url_record = Record.objects.filter(short_url=shortened_part).first()

        assert url_record.request_times == 3