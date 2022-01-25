from rest_framework.decorators import api_view
from rest_framework.response import Response
from config.settings import DEBUG

# from accounts.models import User
# from api.auth.serializers import UserSerializer


# @api_view(['GET'])
# def get_me(request):
#     # if request.user.is_authenticated:
#     #     user = UserSerializer(request.user, many=False).data
#     # else:
#     #     user = 'You are not authenticated'
#     user = 'You are not authenticated'
#     return Response(user)


@api_view(['GET'])
def overview(request):
    if DEBUG:
        url_v1 = "http://127.0.0.1:8000/api/v1"
    else:
        url_v1 = "https://musofir.pythonanywhere.com/api/v1"
    urls = {
        # 'my self': url_v1 + '/get-me/',
        'country': {
            'countries list': url_v1 + '/location/country/',
            'country create': url_v1 + '/location/country/create/',
            'country detail': url_v1 + '/location/country/{id}/',
            'country update': url_v1 + '/location/country/{id}/update/',
            'country delete': url_v1 + '/location/country/{id}/delete/',
        },
        'city': {
            'cities list': url_v1 + '/location/city/',
            'city create': url_v1 + '/location/city/create/',
            'city detail': url_v1 + '/location/city/{id}/',
            'city update': url_v1 + '/location/city/{id}/update/',
            'city delete': url_v1 + '/location/city/{id}/delete/',
        },
        'images': {
            'images list': url_v1 + '/image/',
            'image create': url_v1 + '/image/create/',
            'image detail': url_v1 + '/image/{id}/',
            'image update': url_v1 + '/image/{id}/update/',
            'image delete': url_v1 + '/image/{id}/delete/',

        },
        'flat': {
            'flats list': url_v1 + '/flat/',
            'flat create': url_v1 + '/flat/create/',
            'flat detail': url_v1 + '/flat/{id}/',
            'flat update': url_v1 + '/flat/{id}/update/',
            'flat delete': url_v1 + '/flat/{id}/delete/',
        },
        'job': {
            'jobs list': url_v1 + '/job/',
            'job create': url_v1 + '/job/create/',
            'job detail': url_v1 + '/job/{id}/',
            'job update': url_v1 + '/job/{id}/update/',
            'job delete': url_v1 + '/job/{id}/delete/',
        },
        'embassy': {
            'embassies list': url_v1 + '/embassy/',
            'embassy create': url_v1 + '/embassy/create/',
            'embassy detail': url_v1 + '/embassy/{id}/',
            'embassy update': url_v1 + '/embassy/{id}/update/',
            'embassy delete': url_v1 + '/embassy/{id}/delete/',
        },
        'canteen': {
            'canteens list': url_v1 + '/canteen/',
            'canteen create': url_v1 + '/canteen/create/',
            'canteen detail': url_v1 + '/canteen/{id}/',
            'canteen update': url_v1 + '/canteen/{id}/update/',
            'canteen delete': url_v1 + '/canteen/{id}/delete/',
        }
    }

    return Response(urls)
