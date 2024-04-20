from rest_framework_simplejwt.authentication import JWTAuthentication
from django.conf import settings

class CustomAuthentication(JWTAuthentication):
    """Custom authentication class"""

    def authenticate(self, request):
        header = self.get_header(request)
        raw_token = None

        # Check for cookie first if configured in settings
        if settings.SIMPLE_JWT['AUTH_COOKIE']:
            raw_token = request.COOKIES.get(settings.SIMPLE_JWT['AUTH_COOKIE'])

        # Check for header if cookie is not found or not configured
        if not raw_token:
            if header is None:
                return None  # If header is None, authentication cannot proceed
            raw_token = self.get_raw_token(header)

        if raw_token is None:
            return None

        validated_token = self.get_validated_token(raw_token)
        return self.get_user(validated_token), validated_token
