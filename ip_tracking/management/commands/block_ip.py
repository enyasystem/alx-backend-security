
from django.core.management.base import BaseCommand
from ip_tracking.models import BlockedIP

class Command(BaseCommand):
    help = 'Add an IP address to the blocked list'
    
    def add_arguments(self, parser):
        # Accept an IP address as a command-line argument
        parser.add_argument('ip_address', type=str, help='The IP address to block')

    def handle(self, *args, **options):
        ip_address = options['ip_address']
        # Create a new BlockedIP entry if not existing
        obj, created = BlockedIP.objects.get_or_create(ip_address=ip_address)
        if created:
            self.stdout.write(self.style.SUCCESS(f'Successfully blocked IP address: {ip_address}'))
        else:
            self.stdout.write(self.style.WARNING(f'IP address {ip_address} is already blocked.'))
