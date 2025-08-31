from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

app_name = 'users'

# User
urlpatterns = [

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)