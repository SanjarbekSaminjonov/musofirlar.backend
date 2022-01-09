from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view()
def overview(request):
    urls = {
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
        }
    }
    return Response(urls)
