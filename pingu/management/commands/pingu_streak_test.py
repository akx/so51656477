from datetime import timedelta
from django.core.management import BaseCommand
from django.utils.timezone import now
from pingu.models import Ping
import time

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        t0 = time.time()
        entries = list(Ping.objects.filter(created__gt=now() - timedelta(days=1)).streaks())
        t1 = time.time()
        print(t1 - t0)
        for start, end in entries:
            print(start, end)
            start_ts, start_status = start
            if end:
                end_ts, end_status = end
                end_formatted = '%s at %s' % (end_status, end_ts.isoformat())
            else:
                end_formatted = 'still %s' % start_status
            #print('%s at %s -> %s' % (
            #    start_status, start_ts.isoformat(),
            #    end_formatted,
            #))