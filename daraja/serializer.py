from django.forms import CharField
from rest_framework import serializers
import json
from django.core import serializers as sr

class MakePaymentSerializer(serializers.Serializer):
    amount = serializers.CharField()
    phone_number = serializers.CharField()