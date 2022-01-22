from URLShortenerApp.models import URLRecords
from rest_framework import serializers

class URLRecordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = URLRecords
        fields = "__all__"
        extra_kwargs = {
            "long_url": {"required": True},
            "short_url": {"required": True},}
