from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate

def get_tokens_for_user(user):
    """
    Generate access and refresh tokens for the user.
    """
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

def authenticate_user(email, password):
    """
    Authenticate user and return tokens if valid.
    """
    user = authenticate(email=email, password=password)
    if user:
        return get_tokens_for_user(user)
    return None
