from django.db import models
from apps.users.models import User
from apps.currencies.models import Currency


class Transaction(models.Model):
    user = models.ForeignKey(User, related_name='user', on_delete=models.CASCADE, null=True)
    recipient = models.ForeignKey(User, related_name='user_recipient', on_delete=models.CASCADE, null=True)
    sender = models.ForeignKey(User, related_name='user_sender', on_delete=models.CASCADE, null=True)
    currency = models.ForeignKey(Currency, on_delete=models.SET_NULL, null=True)
    status = models.CharField(default='', max_length=60)
    amount = models.DecimalField(max_digits=11, decimal_places=2)

    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
