from rest_framework.generics import DestroyAPIView
from rest_framework import generics
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.generics import RetrieveAPIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import WebhookEvent
from .serializers import WebhookEventSerializer
from .tasks import fire_webhook 

class WebhookEventCreateView(APIView):
    def post(self, request, *args, **kwargs):
        existing_webhook = WebhookEvent.objects.filter(url=request.data['url']).first()

        if existing_webhook:
            return Response({"error": "Webhook with this URL already exists."}, status=status.HTTP_400_BAD_REQUEST)

        serializer = WebhookEventSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


class FireEventView(APIView):
    def post(self, request, *args, **kwargs):
        company_id = "demo_company2"
        
        active_webhook = WebhookEvent.objects.filter(company_id=company_id).first()
        # print(active_webhook.url, active_webhook.headers)
        if active_webhook.is_active:
            # Trigger the Celery task to fire the webhook
            result = fire_webhook.apply_async(args=[company_id, active_webhook.url, active_webhook.headers or {}])
            print(active_webhook.company_id,active_webhook.url,active_webhook.headers)
            # Wait for the task to complete and get the result
            result_data = result.get()

            return Response({"message": "Webhook request initiated successfully!", "result": result_data}, status=status.HTTP_200_OK)

        return Response({"error": "No active webhook found for the specified company."}, status=status.HTTP_404_NOT_FOUND)


class WebhookEventListView(generics.ListAPIView):
    queryset = WebhookEvent.objects.all()
    serializer_class = WebhookEventSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    

class WebhookEventRetrieveView(RetrieveAPIView):
    queryset = WebhookEvent.objects.all()
    serializer_class = WebhookEventSerializer
    lookup_field = '_id'


class WebhookEventUpdateView(RetrieveUpdateAPIView):
    queryset = WebhookEvent.objects.all()
    serializer_class = WebhookEventSerializer
    lookup_field = '_id'


class WebhookEventDeleteView(DestroyAPIView):
    queryset = WebhookEvent.objects.all()
    serializer_class = WebhookEventSerializer
    lookup_field = '_id'

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({"message": "Webhook deleted successfully!"}, status=status.HTTP_204_NO_CONTENT)