from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from django.shortcuts import redirect


def home(request):
    return redirect('overview')


urlpatterns = [
    path('men-admin/', admin.site.urls),
    path('api/v1/', include('api.home.urls')),
    path('', home, name='home'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
