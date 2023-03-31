from django.db import models
from django.utils.crypto import get_random_string


class ShortURL(models.Model):
    original_url = models.URLField(max_length=255)
    short_code = models.CharField(max_length=6, unique=True)

    def save(self, *args, **kwargs):
        if not self.short_code:
            self.short_code = get_random_string(length=6)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.short_code
