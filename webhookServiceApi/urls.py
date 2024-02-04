from django.urls import path
from .views import WebhookEventCreateView, FireEventView, WebhookEventListView, WebhookEventRetrieveView, WebhookEventDeleteView, WebhookEventUpdateView

urlpatterns = [
    path('webhooks/', WebhookEventCreateView.as_view(), name='webhook-event-create'),
    path('webhooks/all/', WebhookEventListView.as_view(), name='webhook-event-list'),
    path('webhooks/<uuid:_id>/', WebhookEventRetrieveView.as_view(), name='webhook-event-retrieve'),  # Use 'uuid' type
    path('fire-event/', FireEventView.as_view(), name='fire-event'),
    path('webhooks/<uuid:_id>/delete/', WebhookEventDeleteView.as_view(), name='webhook-event-delete'),
    path('webhooks/<uuid:_id>/update/', WebhookEventUpdateView.as_view(), name='webhook-event-update')
]