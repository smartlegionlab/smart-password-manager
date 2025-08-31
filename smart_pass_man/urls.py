from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from smart_pass_man.views.smart_password_create import smart_password_create_view
from smart_pass_man.views.smart_password_delete import smart_password_delete_view
from smart_pass_man.views.smart_password_generate import smart_password_generate_view
from smart_pass_man.views.smart_password_list import smart_password_list_view

app_name = 'smart_password_manager'

# User
urlpatterns = [
    path('', smart_password_list_view, name='smart_password_list'),
    path('create/', smart_password_create_view, name='smart_password_create'),
    path('<int:smart_pass_id>/delete/', smart_password_delete_view, name='smart_password_delete'),
    path('<int:smart_pass_id>/generate/', smart_password_generate_view, name='smart_password_generate'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
