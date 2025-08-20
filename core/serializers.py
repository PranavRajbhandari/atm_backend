from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Account, Transaction


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email']


class AccountSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)


    class Meta:
        model = Account
        fields = ['id', 'user', 'balance']


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['id', 'txn_type', 'amount', 'balance_after', 'note', 'created_at']


class MoneyActionSerializer(serializers.Serializer):
    amount = serializers.DecimalField(max_digits=12, decimal_places=2)


    class TransferSerializer(serializers.Serializer):
        to_username = serializers.CharField()
        amount = serializers.DecimalField(max_digits=12, decimal_places=2)
        # username