import logging
from django.shortcuts import render
from django.http import JsonResponse
from listener.models import TransferEvent
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.decorators import api_view

logger = logging.getLogger(__name__)

@api_view(['GET']) #This is just a temporary basic authentication method. Please use a more secure authentication method, such as OAuth2 with Django REST Framework, especially for production
def get_transfer_history(request, token_id):
    try:
        events = TransferEvent.objects.filter(token_id=token_id)
        
        if not events.exists():
            logger.error(f"No events found for this token: {token_id}")
            return JsonResponse({"message": f"No events found for this token: {token_id}"}, status = 404)

        eventData = [
            {
                "token_id": event.token_id,
                "from_address": event.from_address,
                "to_address": event.to_address,
                "transaction_hash": event.transaction_hash,
                "block_number": event.block_number,
            }
            for event in events
        ]
        return JsonResponse(eventData, safe=False)
    except ObjectDoesNotExist:
        logger.error(f"Token not found.")
        return JsonResponse({"message": "Token ID not found"}, status=404)
    except Exception as e:
        logger.exception(f"Error retrieving transfer history: {e}")
        return JsonResponse({"error": "Internal server error"}, status=500)