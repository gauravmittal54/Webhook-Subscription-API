from django.db import models
from django.utils import timezone

class WebhookSubscription(models.Model):
    company_id = models.CharField(max_length=255, primary_key=True)
    url = models.URLField()
    events = models.JSONField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"WebhookSubscription {self.company_id}"

class WebhookEvent(models.Model):
    webhook_url = models.URLField(primary_key=True)
    events = models.JSONField()
    registered_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"WebhookEvent {self.webhook_url}"
