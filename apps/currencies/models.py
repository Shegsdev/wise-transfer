from django.db import models


class Currency(models.Model):
    name = models.CharField(max_length=60)
    symbol = models.CharField(max_length=60)
    short_code = models.CharField(max_length=10)

    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
