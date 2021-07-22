from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import NumberSerializer
from .models import Number


@api_view(['GET'])
def number_list(request):
    """
        List all numbers as a test to see if this works.
    """
    if request.method == 'GET':
        sets = Number.objects.all()
        serializer = NumberSerializer(sets, many=True)
        return Response(serializer.data)


@api_view(['GET', 'POST'])
def addition(request):
    """
    This function takes two numbers from the input and returns the sum of them.
    Input example: {"input": "100 + 4"}
    Output: {"num_1": [first number provided], "num_2": [second number provided], "total": [total of the two numbers]}
    The numbers are all integers.
    """
    if request.method == 'GET':
        return Response(f"Welcome to the API! Please provide input in the format as explained above.")
    else:
        try:
            request_data = request.data["input"]
            request_data = request_data.replace(" ", "").split("+")
            request_data = [int(x) for x in request_data]
            data = {"num_1": request_data[0],
                    "num_2": request_data[1],
                    "total": sum(request_data)}
        except ValueError:
            content = {'Error message': "Please only provide integers in the string."}
            return Response(content, status=status.HTTP_400_BAD_REQUEST)
        except:
            content = {'Error message': "Something unexpected went wrong. "
                                        "Please provide input in the format as explained above."}
            return Response(content, status=status.HTTP_400_BAD_REQUEST)

        serializer = NumberSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
