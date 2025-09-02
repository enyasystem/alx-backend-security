from django.db import models

# Create your models here.
class RequestLog(models.Model):
    # Stores the IP address of the requester
    ip_address = models.GenericIPAddressField()
    # Stores the path that was requested
    path = models.CharField(max_length=255)

def __str__(self):
    # Helpful for debugging and thhe admin display
    return f"{self.ip_address} at {self.timestamp} requested {self.path}"
