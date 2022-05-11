import base64
from django.conf import settings

def generate_password(dates):
    data_to_encode = settings.BUSNESS_SHORT_CODE+settings.LIPANAMPESA_PASSKEY+dates 
    # data_to_encode = settings.CONSUMER_KEY+settings.CONSUMER_SECRETE+dates
    print(f'KEY {settings.CONSUMER_KEY}  SECRET {settings.CONSUMER_SECRETE}')

    encoded_string = base64.b64encode(data_to_encode.encode())
    decoded_passkey = encoded_string.decode("utf-8")
    return decoded_passkey