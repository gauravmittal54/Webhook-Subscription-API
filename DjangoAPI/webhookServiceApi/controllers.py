from django.utils import timezone
from rest_framework import status
from webhookServiceApi.models import WebhookEvent
from webhookServiceApi.serializers import WebhookEventSerializer

def create_webhook_event_registration_controller(event_data):
    try:
        if not event_data.get('webhook_url') or not event_data.get('events'):
            return {"error": "Webhook URL and events are required"}, status.HTTP_400_BAD_REQUEST
        serializer = WebhookEventSerializer(data=event_data)
        print('valid')
        webhook_event = serializer.save()
        response_data = {
            "id": str(webhook_event.id),
            "webhook_url": webhook_event.webhook_url,
            "events": webhook_event.events,
            "registered_at": webhook_event.registered_at.timestamp()
        }
        return response_data, status.HTTP_201_CREATED
    except Exception as e:
        return {"error": e}, status.HTTP_500_INTERNAL_SERVER_ERROR
