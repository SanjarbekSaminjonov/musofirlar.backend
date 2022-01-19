from rest_framework.decorators import api_view
from rest_framework.response import Response
from accounts.models import User
# from api.auth.serializers import UserSerializer


@api_view()
def get_me(request):
    # if request.user.is_authenticated:
    #     user = UserSerializer(request.user, many=False).data
    # else:
    #     user = 'You are not authenticated'
    user = 'You are not authenticated'
    return Response(user)


@api_view()
def overview(request):
    urls = {
        'my self': '/get-me',

        'country': {
            'countries list': '/country',
            'country create': '/country/create',
            'country detail': '/country/{id}',
            'country update': '/country/{id}/update',
            'country delete': '/country/{id}/delete',
        },

        'city': {
            'cities list': '/city',
            'city create': '/city/create',
            'city detail': '/city/{id}',
            'city update': '/city/{id}/update',
            'city delete': '/city/{id}/delete',
        },
    }

    return Response(urls)
