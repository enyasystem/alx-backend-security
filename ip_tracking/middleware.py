from django.utils import timezone
from .models import RequestLog

class IPLoggingMiddleware:
    """
    Middleware to log IP addresses of incoming requests.
    """
    def __init__(self, get_response):
        self.get_reponse = get_response
        
    def __call__(self, request):
        # Get the IP address from request.META
        ip_address = request.META.get('REMOTE_ADDR', '')
        # Log the request details to the database
        RequestLog.objects.create(
            ip_address=ip_address,
            timestamp=timezone.now(),
            path=request.path
        )
        # Continue processing the request
        response = self.get_response(request)
        return response
