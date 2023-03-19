from django.shortcuts import redirect
from django.core.cache import cache
from django.db import IntegrityError
from rest_framework import views, status
from rest_framework.response import Response
from shortener.models import Record
from shortener.serializers import RecordSerializer
from shortener.utils import transform

class ShortenView(views.APIView):
    def post(self, request):
        long_url = request.data.get("long_url")
        url_record = Record.objects.filter(long_url=long_url)

        if not long_url:
            return Response({"message":"Please Enter The URL !"}, status=status.HTTP_400_BAD_REQUEST)
        
        if url_record:
            # Refresh the data in cache
            cache.set(f"url_record_{url_record.first().short_url}", url_record, 30)
            return Response(url_record.values()[0], status=status.HTTP_303_SEE_OTHER)

        short_url = transform.create_short_url(Record())

        # Add short_url as parameter to request data
        request.data._mutable = True
        request.data["short_url"] = short_url
        request.data._mutable = False

        serializer = RecordSerializer(data=request.data)

        if serializer.is_valid():
            try:
                serializer.save()
            except IntegrityError as e:
                serializer.save(short_url=transform.create_short_url(Record()))

            url_record = Record.objects.filter(long_url=long_url)

            # Set the data in cache for later retrieve
            cache.set(f"url_record_{short_url}", url_record, 30)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        else:
            if "long_url" in serializer.errors.keys() and "Longer URL already exists" in serializer.errors["long_url"][0]:
                url_record = Record.objects.filter(long_url=long_url)

                if url_record:
                    return Response(url_record.values()[0], status=status.HTTP_303_SEE_OTHER)
                else:
                    Response(serializer.errors, status=status.HTTP_409_CONFLICT)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RedirectView(views.APIView):
    def get(self, request, shortened_part):
        url_record_cache = cache.get(f"url_record_{shortened_part}")

        # Retrieve the data from cache
        if url_record_cache:
            url_record = url_record_cache
        else:
            url_record = Record.objects.filter(short_url=shortened_part)

        if not url_record:
            return Response({"message":"The URL Not Found !"}, status=status.HTTP_404_NOT_FOUND)

        url_record_obj = url_record.first()

        # Increase the shirt URL requested times
        url_record_obj.request_times += 1
        url_record_obj.save()

        # Refresh the data in cache
        cache.set(f"url_record_{shortened_part}", url_record, 30)

        long_url = url_record_obj.long_url

        # Redirect to the original URL
        return redirect(long_url)