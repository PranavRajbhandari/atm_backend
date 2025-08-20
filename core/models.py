# atm_backend/core/models.py
from django.db import models
from django.contrib.auth.models import User


class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='account')
    balance = models.DecimalField(max_digits=12, decimal_places=2, default=0)


def __str__(self):
    return f"{self.user.username} - {self.balance}"


class Transaction(models.Model):
    DEPOSIT = 'DEPOSIT'
    WITHDRAW = 'WITHDRAW'
    TRANSFER_IN = 'TRANSFER_IN'
    TRANSFER_OUT = 'TRANSFER_OUT'
    TYPE_CHOICES = [
    (DEPOSIT, 'Deposit'),
    (WITHDRAW, 'Withdraw'),
    (TRANSFER_IN, 'Transfer In'),
    (TRANSFER_OUT, 'Transfer Out'),
    ]


    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='transactions')
    txn_type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    balance_after = models.DecimalField(max_digits=12, decimal_places=2)
    note = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ['-created_at']


    def __str__(self):
        return f"{self.account.user.username} {self.txn_type} {self.amount}"