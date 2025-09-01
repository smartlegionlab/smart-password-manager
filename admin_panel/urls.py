from django.urls import path

from admin_panel.views.panel import admin_panel_view
from admin_panel.views.site_config.site_config_detail import site_config_detail_view
from admin_panel.views.site_config.site_config_update import site_config_update_view
from admin_panel.views.system_info.system_info_detail import system_info_detail_view
from admin_panel.views.system_info.system_info_update import system_info_update_view

app_name = 'admin_panel'

# Admin panel
urlpatterns = [
    path('', admin_panel_view, name='admin_panel'),
]

# Site Config
urlpatterns += [
    path('site-config/', site_config_detail_view, name='site_config'),
    path('site-config/update/', site_config_update_view, name='site_config_update'),
]

# System info
urlpatterns += [
    path('system-info/', system_info_detail_view, name='system_info'),
    path('system-info/update/', system_info_update_view, name='system_info_update'),
]