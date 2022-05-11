import requests
from requests import auth
from requests.auth import HTTPBasicAuth
from django.conf import settings

def generate_token():
    res = requests.get(settings.ACCESS_TOKEN_URL, auth=HTTPBasicAuth(settings.CONSUMER_KEY, settings.CONSUMER_SECRETE))   
    json_response = res.json()
    acess_token = json_response['access_token']
    
    return acess_token 
