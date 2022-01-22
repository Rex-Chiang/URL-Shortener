from URLShortenerApp.models import URLRecords
from URLShortenerApp.serializers import URLRecordsSerializer
from rest_framework import views
from rest_framework import status
from rest_framework.response import Response
from URLShortenerApp.utils import transform
from django.shortcuts import redirect

class ShortenURLView(views.APIView):
    def post(self, request):
        long_url = request.data.get("long_url")
        url_record = URLRecords.objects.filter(long_url = long_url)

        if not long_url:
            return Response("Please Enter The URL !", status = status.HTTP_400_BAD_REQUEST)
        if url_record:
            return Response(url_record.values(), status = status.HTTP_303_SEE_OTHER)

        short_url = transform.create_short_url(URLRecords())
        # Add short_url as parameter to request data
        request.data._mutable = True
        request.data["short_url"] = short_url
        request.data._mutable = False
        serializer = URLRecordsSerializer(data = request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class RedirectURLView(views.APIView):
    def get(self, request, shortened_part):
        url_record = URLRecords.objects.filter(short_url = shortened_part).first()

        if not url_record:
            return Response("The URL Not Found !", status = status.HTTP_404_NOT_FOUND)
        # Increase the shirt URL requested times
        url_record.request_times += 1
        url_record.save()

        long_url = url_record.long_url
        # Redirect to the original URL
        return redirect(long_url)