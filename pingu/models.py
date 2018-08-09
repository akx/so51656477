from django.db import models
from django.utils import timezone

class PingQuerySet(models.QuerySet):
    def streaks(self):
        queryset = self.values_list('created', 'online').order_by('created')
        entry = queryset.first()
        while entry:
            next_entry = queryset.filter(created__gt=entry[0], online=(not entry[1])).first()
            yield (entry, next_entry)
            entry = next_entry


class Ping(models.Model):
    online = models.BooleanField()
    created = models.DateTimeField(db_index=True, default=timezone.now)
    objects = PingQuerySet.as_manager()