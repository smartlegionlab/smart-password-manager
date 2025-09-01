from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from admin_panel.views.page_403 import custom_403_view

handler403 = custom_403_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('users.urls')),
    path('smart-password-manager/', include('smart_pass_man.urls')),
    path('admin-panel/', include('admin_panel.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
