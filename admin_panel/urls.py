from django.urls import path

from admin_panel.views.auth_logs.auth_log_delete import auth_log_delete_view
from admin_panel.views.auth_logs.auth_log_detail import auth_log_detail_view
from admin_panel.views.auth_logs.auth_log_get_ip_info import auth_log_get_ip_info_view
from admin_panel.views.auth_logs.auth_log_list import auth_log_list_view
from admin_panel.views.auth_logs.auth_logs_clear import auth_logs_clear_view
from admin_panel.views.panel import admin_panel_view
from admin_panel.views.site_config.site_config_detail import site_config_detail_view
from admin_panel.views.site_config.site_config_update import site_config_update_view
from admin_panel.views.system_info.system_info_detail import system_info_detail_view
from admin_panel.views.system_info.system_info_update import system_info_update_view
from admin_panel.views.users.user_block import user_block_view
from admin_panel.views.users.user_create import user_create_view
from admin_panel.views.users.user_delete import user_delete_view
from admin_panel.views.users.user_detail import user_detail_view
from admin_panel.views.users.user_list import user_list_view
from admin_panel.views.users.user_update import user_update_view

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

# Users
urlpatterns += [
    path('users/', user_list_view, name='admin_user_list'),
    path('users/<int:pk>/detail/', user_detail_view, name='admin_user_detail'),
    path('users/create/', user_create_view, name='admin_user_create'),
    path('users/<int:pk>/update/', user_update_view, name='admin_user_update'),
    path('users/<int:pk>/delete/', user_delete_view, name='admin_user_delete'),
    path('users/<int:pk>/block/', user_block_view, name='admin_user_block'),
]

# User auth logs
urlpatterns += [
    path('auth-logs/<int:pk>/history/', auth_log_list_view, name='admin_user_auth_logs'),
    path('auth-logs/<int:pk>/clear/', auth_logs_clear_view, name='admin_user_auth_log_all_delete'),
    path('auth-logs/<int:log_id>/delete/', auth_log_delete_view, name='admin_user_auth_log_delete'),
    path('auth-logs/<int:log_id>/detail/', auth_log_detail_view, name='admin_user_auth_log_detail'),
    path('auth-logs/<int:log_id>/refresh/', auth_log_get_ip_info_view, name='admin_user_auth_refresh_ip_info'),
]