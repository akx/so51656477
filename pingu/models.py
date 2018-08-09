from django.db import models
from django.utils import timezone


class Ping(models.Model):
    online = models.BooleanField()
    created = models.DateTimeField(db_index=True, default=timezone.now)
