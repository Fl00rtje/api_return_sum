from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import NumberSerializer
from .models import Number


@api_view(['GET'])
def number_list(request, format=None):
    """
        List all numbers as a test to see if this works.
    """
    if request.method == 'GET':
        sets = Number.objects.all()
        serializer = NumberSerializer(sets, many=True)
        return Response(serializer.data)
