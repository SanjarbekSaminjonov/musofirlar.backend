from rest_framework.decorators import api_view
from rest_framework.response import Response


# from accounts.models import User
# from api.auth.serializers import UserSerializer


@api_view(['GET'])
def get_me(request):
    # if request.user.is_authenticated:
    #     user = UserSerializer(request.user, many=False).data
    # else:
    #     user = 'You are not authenticated'
    user = 'You are not authenticated'
    return Response(user)


@api_view(['GET'])
def overview(request):
    urls = {
        'my self': 'get-me/',
        'country': {
            'countries list': 'location/country/',
            'country create': 'location/country/create/',
            'country detail update delete': 'location/country/{id}/',
        },
        'city': {
            'cities list': 'location/city/',
            'city create': 'location/city/create/',
            'city detail update delete': 'location/city/{id}/',
        },
        'flat': {
            'flats list': 'flat/',
            'flat create': 'flat/create/',
            'flat detail update delete': 'flat/{id}/',
        },
        'job': {
            'jobs list': 'job/',
            'job create': 'job/create',
            'job detail update delete': 'job/{id}/',
        },
    }

    return Response(urls)
