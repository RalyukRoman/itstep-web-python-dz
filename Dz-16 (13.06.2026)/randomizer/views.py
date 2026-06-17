from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

import random


@api_view(['GET'])
def get_random_numbers(request):
    """Отримати випадкове число або список випадкових чисел"""

    try:
        min = int(request.GET.get('min', -99999))
        max = int(request.GET.get('max',  99999))
        count = int(request.GET.get('count', 1))
    except ValueError:
        return Response(
            {'error': 'Parameters must be valid integers.'}, 
            status=status.HTTP_400_BAD_REQUEST
        )

    if (min > max):
        return Response(
            {'error': 'Min cannot be greater than Max.'}, 
            status=status.HTTP_400_BAD_REQUEST
        )
    
    if count < 1:
        return Response(
            {'error': 'Count must be at least 1'}, 
            status=status.HTTP_400_BAD_REQUEST
        )

    if count == 1:
        rand = random.randint(min, max)
        return Response(
            rand, 
            status=status.HTTP_200_OK
        )
    else:
        rand_list = [random.randint(min, max) for _ in range(count)]
        return Response(
            rand_list, 
            status=status.HTTP_200_OK
        )



