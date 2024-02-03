from rest_framework import serializers
from .models import WebhookSubscription, WebhookEvent

class WebhookSubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = WebhookSubscription
        fields = ('company_id', 'url', 'events', 'is_active', 'created_at', 'updated_at')

class WebhookEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = WebhookEvent
        fields = ('webhook_url', 'events', 'registered_at')
