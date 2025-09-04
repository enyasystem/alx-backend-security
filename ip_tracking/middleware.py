from .models import RequestLog
from django.http import HttpResponseForbidden
from .models import BlockedIP

class IPLoggingMiddleware:
    """
    Middleware to log IP address and path of every request.
    """
    def __init__(self, get_response):
        # This method is called only once, when the server starts.
        self.get_response = get_response

    def __call__(self, request):
        # This method is called for every request.
        ip_address = request.META.get('REMOTE_ADDR', '')
        RequestLog.objects.create(
            ip_address=ip_address,
            path=request.path
        )
        
        if BlockedIP.objects.filter(ip_address=ip_address).exists():
            # Return a 403 Forbidden response if the IP is blocked
            return HttpResponseForbidden("Your IP address is blocked.")
        # Otherwise, proceed with the request
        response = self.get_response(request)
        return response
