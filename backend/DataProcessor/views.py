from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['POST'])
def process_data(request):
    data = request.data

    # data is in form
    """ const data = {
            location,
            minPrice,
            maxPrice,
            pets,
            selectedDate
        }; """

   
    return Response({'result': 'success'})