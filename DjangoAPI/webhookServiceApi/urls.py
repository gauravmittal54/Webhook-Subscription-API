from django.urls import path
from .views import (
    # create_webhook_subscription,
    # update_webhook_subscription,
    # delete_webhook_subscription,
    # get_all_webhook_subscriptions,
    # get_single_webhook_subscription,
    create_webhook_event_registration,
    # get_available_webhook_events
)

urlpatterns = [
    # path('webhooks/', create_webhook_subscription, name='create_webhook_subscription'),
    # path('webhooks/<str:id>/', update_webhook_subscription, name='update_webhook_subscription'),
    # path('webhooks/<str:id>/', delete_webhook_subscription, name='delete_webhook_subscription'),
    # path('webhooks/', get_all_webhook_subscriptions, name='get_all_webhook_subscriptions'),
    # path('webhooks/<str:id>/', get_single_webhook_subscription, name='get_single_webhook_subscription'),

    path('webhook-events/', create_webhook_event_registration, name='create_webhook_event_registration'),
    # path('webhook-events/', get_available_webhook_events, name='get_available_webhook_events'),
]
