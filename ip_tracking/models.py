from django.db import models

# Create your models here.
class RequestLog(models.Model):
    # Stores the IP address of the requester
    ip_address = models.GenericIPAddressField(unique=True)
    # Stores the path that was requested
    path = models.CharField(max_length=255)

    def __str__(self):
        # Helpful for debugging and the admin display
        return f"{self.ip_address} - {self.path}"
