from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser

from features.cards.models import Card
from features.cards.serializers import CardSerializer


@api_view(['GET', 'POST', 'DELETE'])
def cards_view(request):
    if request.method == 'GET':
        cards = Card.objects.all()
        tutorials_serializer = CardSerializer(cards, many=True)
        return JsonResponse(tutorials_serializer.data, safe=False)

    elif request.method == 'POST':
        card_data = JSONParser().parse(request)
        cards_serializer = CardSerializer(data=card_data)
        if cards_serializer.is_valid():
            cards_serializer.save()
            return JsonResponse(cards_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(cards_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        count = Card.objects.all().delete()
        return JsonResponse({'message': '{} Tutorials were deleted successfully!'.format(count[0])},
                            status=status.HTTP_204_NO_CONTENT)
