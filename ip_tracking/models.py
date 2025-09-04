from django.db import models

# Create your models here.
# Model to log requests (already present)
class RequestLog(models.Model):
    # Stores the IP address of the requester
    ip_address = models.GenericIPAddressField()
    # Stores the path that was requested
    path = models.CharField(max_length=255)
    # Stores the country of the requester (geolocation)
    country = models.CharField(max_length=100, blank=True, null=True)
    # Stores the city of the requester (geolocation)
    city = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # Display IP, country, and city for easier debugging
        return f"{self.ip_address} ({self.country}, {self.city})"

# Model to store blocked IP addresses for blacklisting
class BlockedIP(models.Model):
    """
    Model to store IP addresses that are blocked from accessing the site.
    """
    ip_address = models.GenericIPAddressField()

    def __str__(self):
        # Display the IP address in admin and debugging
        return self.ip_address

class SuspiciousIP(models.Model):
    ip_address = models.GenericIPAddressField()
    reason = models.CharField(max_length=255)
    flagged_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.ip_address} - {self.reason}"
