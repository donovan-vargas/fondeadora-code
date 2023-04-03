from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from core.models import ShortURL

SHORTED_URL = reverse('shorten-url')


def redirect_url(short_code):
    return reverse('redirect-url', args=[short_code])


class ShortURLApiTest(TestCase):
    """Test short url API"""

    def setUp(self):
        self.url_to_short = 'https://www.google.com/'
        self.client = APIClient()

    def test_create_short_url(self):
        """Test create a new short url"""
        payload = {
            'original_url': self.url_to_short
        }
        res = self.client.post(SHORTED_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertIn('short_code', res.data)
        short_code = res.data['short_code']
        obj_short_url = ShortURL.objects.get(short_code=short_code)
        self.assertEqual(obj_short_url.original_url, payload['original_url'])

    def test_redirect_to_url(self):
        obj_short_url = ShortURL.objects.create(
            original_url=self.url_to_short,
            short_code='abcde'
        )
        url = redirect_url(obj_short_url.short_code)
        res = self.client.get(url)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertIn('original_url', res.data)
        self.assertEqual(res.data['original_url'], self.url_to_short)

    def test_redirect_to_url_with_invalid_shortcode(self):
        url = redirect_url('invalid')
        res = self.client.get(url)
        self.assertEqual(res.status_code, status.HTTP_404_NOT_FOUND)

    def test_shorten_url_with_invalid_data(self):
        payload = {'original_url': 'invalid-url'}
        res = self.client.post(SHORTED_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_redirect_existing_shortcode(self):
        self.short_url = ShortURL.objects.create(
            original_url=self.url_to_short, short_code='abc123')
        res = self.client.get('/abc123')
        self.assertEqual(res.status_code, status.HTTP_302_FOUND)
        self.assertRedirects(
            res, self.url_to_short, fetch_redirect_response=False)

    def test_redirect_non_existing_shortcode(self):
        res = self.client.get('/does_not_exist')
        self.assertEqual(res.status_code, status.HTTP_404_NOT_FOUND)
