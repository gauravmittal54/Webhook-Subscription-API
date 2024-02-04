from django.db import models
from django.utils import timezone
import uuid

class WebhookEvent(models.Model):
    _id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    company_id = models.CharField(max_length=255)
    url = models.URLField(unique=True)
    headers = models.JSONField(blank=True, null=True)
    events = models.JSONField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"WebhookEvent {self.url}"
