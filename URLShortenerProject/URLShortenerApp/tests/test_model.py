import pytest
from URLShortenerApp.models import URLRecords

pytestmark = pytest.mark.django_db()

class TestModel:
    def test_URLRecords(self):
        assert URLRecords.objects.count() == 3

    def test_URLRecords_create(self):
        url = "https://www.google.com"
        URLRecords.objects.create(long_url = url)
        url_record = URLRecords.objects.filter(long_url = url).first()
        assert URLRecords.objects.count() == 4
        assert url_record.long_url == url
        assert url_record.short_url == ""
        assert url_record.request_times == 0

    def test_URLRecords_retrieve_success(self):
        url = "https://github.com/Rex-Chiang"
        url_record = URLRecords.objects.filter(long_url = url).first()
        assert url_record.long_url == url
        assert len(url_record.short_url) == 6
        assert url_record.request_times == 0

    def test_URLRecords_retrieve_fail(self):
        url = "https://www.google.com"
        url_record = URLRecords.objects.filter(long_url = url).first()
        assert url_record == None