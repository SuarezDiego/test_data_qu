from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from car_rental.models import Statistics


@api_view(['GET'])
def data_statistics(request):
    data = Statistics.objects.last().data
    return Response(data)