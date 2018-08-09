from datetime import timedelta
from django.core.management import BaseCommand
from django.db.transaction import atomic
from django.utils.timezone import now
from pingu.models import Ping
import random

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        n = 100_000
        until = now()
        with atomic():
            for timestamp in (
                until - timedelta(minutes=i * 30)
                for i
                in range(n, 0, -1)
            ):
                Ping.objects.create(created=timestamp, online=(random.random() > .65))