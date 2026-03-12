from datetime import datetime, timedelta
from jwt import DecodeError, decode, encode
from app.core.config import settings

secret = settings.TOKEN_SECRET_KEY
algorithm = settings.TOKEN_ALGORITHM

def create_access_token(data: dict):
    to_encode = data.copy()
    encoded_jwt = encode(to_encode, secret, algorithm=algorithm)

    return encoded_jwt

def get_decoded_data(token: str):
    payload = decode(token, secret, algorithms=algorithm)
    return payload

def token_verify(token):
    try:
        decoded = get_decoded_data(token)
        is_expired = is_token_expired(decoded['expires_at'])
        is_valid = is_token_valid(token)

        if not is_expired and is_valid:
            return True
        else:
            return False
    except Exception as e:
        print("error security: ", e)
        return False

def is_token_expired(expires_at: int, margin_seconds: int = 60):
    current_time = datetime.now().timestamp()
    time_until_expiry = expires_at - current_time
    return time_until_expiry < margin_seconds

def is_token_valid(token):
    """ tobe implemented """    
    return True