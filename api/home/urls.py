from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.overview),
    path('get-me/', views.get_me),
    path('location/', include('api.location.urls')),
    path('flat/', include('api.flat.urls')),
    path('job/', include('api.job.urls')),
    path('embassy/', include('api.embassy.urls')),
    path('canteen/', include('api.canteen.urls')),
]
