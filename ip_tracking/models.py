from django.db import models

# Create your models here.

# Model to log requests (already present)
class RequestLog(models.Model):
    # Stores the IP address of the requester
    ip_address = models.GenericIPAddressField()
    # Stores the path that was requested
    path = models.CharField(max_length=255)

    def __str__(self):
        # Helpful for debugging and the admin display
        return str(self.ip_address)

# Model to store blocked IP addresses for blacklisting
class BlockedIP(models.Model):
    """
    Model to store IP addresses that are blocked from accessing the site.
    """
    ip_address = models.GenericIPAddressField()

    def __str__(self):
        # Display the IP address in admin and debugging
        return self.ip_address
