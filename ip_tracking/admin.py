from django.contrib import admin
from .models import SuspiciousIP, BlockedIP, RequestLog

# Register models for admin interface
admin.site.register(SuspiciousIP)
admin.site.register(BlockedIP)
admin.site.register(RequestLog)
