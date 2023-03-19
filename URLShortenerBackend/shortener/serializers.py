from shortener.models import Record
from rest_framework import serializers

class RecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Record
        fields = "__all__"
        extra_kwargs = {
            "long_url": {"required": True},
            "short_url": {"required": True},}
