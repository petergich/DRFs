# yourapp/middleware.py

from django.http import JsonResponse
from django.utils.deprecation import MiddlewareMixin

class AuthMiddleware(MiddlewareMixin):
    def process_request(self, request):
        # Exclude certain URLs from authentication
        if request.path.startswith('/categories'):
            return None  # Allow access without authentication

        # Check for authentication
        if not request.user.is_authenticated:
            return JsonResponse({'detail': 'Authentication credentials were not provided.'}, status=403)
