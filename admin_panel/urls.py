from django.urls import path

from admin_panel.views.panel import admin_panel_view

app_name = 'admin_panel'

# Admin panel
urlpatterns = [
    path('', admin_panel_view, name='admin_panel'),
]