from .models import Prediction
from .serializers import PredictionSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

import random


@api_view(['GET'])
def get_random_prediction(request):
    """Отримати випадкове передбачення"""

    pks = Prediction.objects.values_list('id', flat=True)

    if pks:
        random_id = random.choice(pks)
        random_prediction = Prediction.objects.filter(pk=random_id).first()
    else:
        random_prediction = None

    if not random_prediction:
        return Response(
            {'error': 'No prediction found'}, 
            status=status.HTTP_404_NOT_FOUND
        )

    serializer = PredictionSerializer(random_prediction)
    
    return Response(
        serializer.data, 
        status=status.HTTP_200_OK
    )
