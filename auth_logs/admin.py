from django.contrib import admin

from auth_logs.models import UserAuthLog

admin.site.register(UserAuthLog)
