
from .models import RequestLog, BlockedIP
from django.http import HttpResponseForbidden
from django.core.cache import cache
import requests



class IPLoggingMiddleware:
    """
    Middleware to log IP address, path, and geolocation of every request using ip-api.com.
    Caches geolocation results for 24 hours to reduce API calls.
    Also blocks requests from blacklisted IPs.
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        ip_address = request.META.get('REMOTE_ADDR', '')
        path = request.path

        # Check if IP is blocked
        if BlockedIP.objects.filter(ip_address=ip_address).exists():
            return HttpResponseForbidden("Your IP address is blocked.")

        # Geolocation caching key
        cache_key = f'geo_{ip_address}'
        geo_data = cache.get(cache_key)

        if not geo_data:
            try:
                # Query ip-api.com for geolocation
                api_url = f'http://ip-api.com/json/{ip_address}'
                response = requests.get(api_url, timeout=5)
                data = response.json()
                geo_data = {
                    'country': data.get('country', ''),
                    'city': data.get('city', '')
                }
            except Exception:
                geo_data = {'country': '', 'city': ''}
            # Cache for 24 hours (86400 seconds)
            cache.set(cache_key, geo_data, timeout=86400)

        # Log the request with geolocation
        RequestLog.objects.create(
            ip_address=ip_address,
            path=path,
            country=geo_data['country'],
            city=geo_data['city']
        )

        response = self.get_response(request)
        return response
