
from rest_framework.response import Response
from rest_framework import generics
from .models import ShortURL
from .serializers import ShortURLSerializer


class ShortenURLView(generics.CreateAPIView):
    """Manage the short url in the database"""
    serializer_class = ShortURLSerializer


class RedirectURLView(generics.RetrieveAPIView):
    """Retrieve the short url"""
    queryset = ShortURL.objects.all()
    lookup_field = 'short_code'

    def retrieve(self, request, *args, **kwargs):
        short_url = self.get_object()
        return Response({'original_url': short_url.original_url})
