from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from users.views.auth.login import login_view
from users.views.auth.logout import logout_view
from users.views.user.avatar_reset import user_avatar_reset_view
from users.views.user.avatar_upload import user_avatar_upload_view
from users.views.auth.password_change import password_change_view
from users.views.auth.password_generate import password_generate_view
from users.views.auth.password_reset import password_reset_view
from users.views.auth.register import register_view
from users.views.auth.two_factor import auth_2fa_view, auth_2fa_check_code
from users.views.user.user_delete import user_delete_view
from users.views.user.user_detail import user_detail_view
from users.views.user.user_update import user_update_view

app_name = 'users'

# User
urlpatterns = [
    path('', user_detail_view, name='user_detail'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('avatar/reset/', user_avatar_reset_view, name='avatar_reset'),
    path('avatar/upload/', user_avatar_upload_view, name='avatar_upload'),
    path('delete/', user_delete_view, name='user_delete'),
    path('update/', user_update_view, name='user_update'),
    path('register/', register_view, name='register'),
    path('auth-2fa/<str:token>/', auth_2fa_view, name='auth_2fa'),
    path('auth-2fa/check/code/', auth_2fa_check_code, name='auth_2fa_check_code'),
    path('password/reset/', password_reset_view, name='password_reset'),
    path('password/change/', password_change_view, name='password_change'),
    path('password/generate/', password_generate_view, name='password_generate'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
