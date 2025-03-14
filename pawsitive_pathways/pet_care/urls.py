from django.urls import path
from .views import service_list, select_service
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("service-list/", service_list, name="service_list"),
    path("select-service/", select_service, name="select_service"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
