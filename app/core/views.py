
from rest_framework.response import Response
from rest_framework import generics
from django.shortcuts import redirect
from django.http import Http404
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


def redirect_to_url(request, short_code):
    """HTML page to redirect automatically """
    try:
        short_url = ShortURL.objects.get(short_code=short_code)
        return redirect(short_url.original_url)
    except ShortURL.DoesNotExist:
        raise Http404('Short code does not exist')
