from django.db import models
from celery import shared_task
from django.utils import timezone
from datetime import timedelta
from django.db import models
from .models import RequestLog, SuspiciousIP

@shared_task
def detect_anomalies():
    now = timezone.now()
    one_hour_ago = now - timedelta(hours=1)

    # Flag IPs with >100 requests/hour
    ip_counts = (
        RequestLog.objects
        .filter(path__isnull=False, ip_address__isnull=False, created_at__gte=one_hour_ago)
        .values('ip_address')
        .annotate(count=models.Count('id'))
        .filter(count__gt=100)
    )
    for entry in ip_counts:
        SuspiciousIP.objects.get_or_create(
            ip_address=entry['ip_address'],
            reason='High request rate (>100/hour)'
        )

    # Flag IPs accessing sensitive paths
    sensitive_paths = ['/admin', '/login']
    logs = RequestLog.objects.filter(path__in=sensitive_paths, created_at__gte=one_hour_ago)
    for log in logs:
        SuspiciousIP.objects.get_or_create(
            ip_address=log.ip_address,
            reason=f"Accessed sensitive path: {log.path}"
        )
