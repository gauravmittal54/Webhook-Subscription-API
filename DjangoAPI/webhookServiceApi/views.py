
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from rest_framework.decorators import api_view

from .controllers import (
    create_webhook_event_registration_controller   
)


@csrf_exempt
@api_view(['POST'])
def create_webhook_event_registration(request):
    if request.method == 'POST':
        event_data = JSONParser().parse(request)
        result, http_status = create_webhook_event_registration_controller(event_data)
        return JsonResponse(result, status=http_status)
