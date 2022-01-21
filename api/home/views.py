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
            'countries list': '/location/country/',
            'country create': '/location/country/create/',
            'country detail': '/location/country/{id}/',
            'country update': '/location/country/{id}/update/',
            'country delete': '/location/country/{id}/delete/',
        },
        'city': {
            'cities list': '/location/city/',
            'city create': '/location/city/create/',
            'city detail': '/location/city/{id}/',
            'city update': '/location/city/{id}/update/',
            'city delete': '/location/city/{id}/delete/',
        },
        'flat': {
            'flats list': '/flat/',
            'flat create': '/flat/create/',
            'flat detail': '/flat/{id}/',
            'flat update': '/flat/{id}/update/',
            'flat delete': '/flat/{id}/delete/',
        },
        'job': {
            'jobs list': '/job/',
            'job create': '/job/create/',
            'job detail': '/job/{id}/',
            'job update': '/job/{id}/update/',
            'job delete': '/job/{id}/delete/',
        },
        'embassy': {
            'embassies list': '/embassy/',
            'embassy create': '/embassy/create/',
            'embassy detail': '/embassy/{id}/',
            'embassy update': '/embassy/{id}/update/',
            'embassy delete': '/embassy/{id}/delete/',
        },
        'canteen': {
            'canteens list': '/canteen/',
            'canteen create': '/canteen/create/',
            'canteen detail': '/canteen/{id}/',
            'canteen update': '/canteen/{id}/update/',
            'canteen delete': '/canteen/{id}/delete/',
        }
    }

    return Response(urls)
