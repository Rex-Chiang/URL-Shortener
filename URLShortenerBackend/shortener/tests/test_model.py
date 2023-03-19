import pytest
from shortener.models import Record

pytestmark = pytest.mark.django_db()

class TestModel:
    def test_record(self):
        assert Record.objects.count() == 0

    def test_record_create(self):
        url = "https://www.google.com"
        Record.objects.create(long_url=url)
        url_record = Record.objects.filter(long_url=url).first()

        assert Record.objects.count() == 1
        assert url_record.long_url == url
        assert url_record.short_url == ""
        assert url_record.request_times == 0

    def test_record_retrieve_success(self):
        url = "https://github.com/Rex-Chiang"
        url_record = Record.objects.filter(long_url=url).first()

        assert url_record.long_url == url
        assert len(url_record.short_url) == 6
        assert url_record.request_times == 0

    def test_recordr_retrieve_fail(self):
        url = "https://www.google.com"
        url_record = Record.objects.filter(long_url=url).first()

        assert url_record == None