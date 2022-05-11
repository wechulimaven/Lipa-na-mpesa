from django.shortcuts import render
import requests

# from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView

from rest_framework.response import Response
from django.http import HttpResponse, JsonResponse
from django.conf import settings
import json
# from django.views.decorators.csrf import csrf_exempt
# from .models import MpesaCallBack, MpesaPayment
from .access_token_encoding import generate_password
from .date_formating import formatDateTime
from .generate_token import generate_token
from .serializer import MakePaymentSerializer


class InitateSTKPush(GenericAPIView):
    serializer_class = MakePaymentSerializer

    def post(self, request, *args, **kwargs):
        serilizer = self.serializer_class(data=request.data)
        serilizer.is_valid(raise_exception=True)

        requestData = request.data
        amount = requestData.get("amount")
        phone = requestData.get("phone_number")

        paymentResponse = self.initiate_mpesa_stk(
            amount=amount, phone=phone)

        return Response(paymentResponse)

    def initiate_mpesa_stk(self, amount: str, phone: str) -> dict:
        access_token = generate_token()
        formated_time = formatDateTime()
        password = generate_password(formated_time)

        headers = {
            "Authorization": "Bearer %s" % access_token
        }

        payload = {
            "BusinessShortCode": "174379",
            "Password": password,
            "Timestamp": formated_time,
            "TransactionType": "CustomerPayBillOnline",
            "Amount": amount,
            "PartyA": phone,
            "PartyB": "174379",
            "PhoneNumber": phone,
            "CallBackURL": "https://posthere.io/386b-43c7-8393",
            "AccountReference": "ONLINE PAYMENT LIMITED",
            "TransactionDesc": "Make payment"
        }

        response = requests.post(
            settings.API_RESOURCE_URL, headers=headers, json=payload)

        string_response = response.text
        string_object = json.loads(string_response)

        if 'errorCode' in string_object:
            print('ERROR', string_object)
            # pass
            return string_object
        else:
            merchant_request_id = string_object["MerchantRequestID"]
            checkout_request_id = string_object["CheckoutRequestID"]
            response_code = string_object["ResponseCode"]
            response_description = string_object["ResponseDescription"]
            customer_message = string_object["CustomerMessage"]

            data = {
                "MerchantRequestID": merchant_request_id,
                "CheckoutRequestID": checkout_request_id,
                "ResponseCode": response_code,
                "ResponseDescription": response_description,
                "CustomerMessage": customer_message,
            }


            return data

