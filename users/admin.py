from django.contrib import admin
from django.utils.html import format_html
from users.models import PasswordResetToken, User, EmailVerificationToken


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'avatar_preview',
        'email', 
        'full_name',
        'is_active', 
        'is_staff', 
        'created_at',
        'is_email_verified'
    )
    
    list_display_links = ('email',)
    
    search_fields = (
        'email', 
        'first_name', 
        'last_name', 
        'id',
    )
    
    list_filter = (
        'is_active', 
        'is_staff', 
        'is_superuser',
        'gender', 
        'created_at',
        'is_email_verified'
    )
    
    ordering = ('-created_at',)
    
    readonly_fields = ('avatar_preview_large', 'created_at', 'updated_at', 'id')
    
    fieldsets = (
        (None, {
            'fields': ('email', 'password', 'is_email_verified')
        }),
        ('Personal Info', {
            'fields': ('first_name', 'last_name', 'gender', 'bio', 'avatar_preview_large')
        }),
        ('Permissions', {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')
        }),
        ('Important Dates', {
            'fields': ('created_at', 'updated_at', 'last_login')
        }),
    )
    
    filter_horizontal = ('groups', 'user_permissions')
    
    def full_name(self, obj):
        return f"{obj.first_name} {obj.last_name}"
    full_name.short_description = 'Full Name'
    
    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False
    
    def avatar_preview(self, obj):
        return self._get_avatar_html(obj, size=50)
    avatar_preview.short_description = 'Avatar'
    
    def avatar_preview_large(self, obj):
        return self._get_avatar_html(obj, size=150)
    avatar_preview_large.short_description = 'Current Avatar'
    
    def _get_avatar_html(self, obj, size=50):
        try:
            avatar_url = obj.get_avatar()
            return format_html(
                '<img src="{}" width="{}" height="{}" style="border-radius: 50%; object-fit: cover;" />',
                avatar_url,
                size,
                size
            )
        except:
            return format_html(
                '<div style="width: {}px; height: {}px; border-radius: 50%; background: #ccc; display: ' \
                'flex; align-items: center; justify-content: center;">No Avatar</div>',
                size,
                size
            )


@admin.register(EmailVerificationToken)
class EmailVerificationTokenAdmin(admin.ModelAdmin):
    list_display = ('token', 'user', 'created_at', 'is_used', 'is_valid_display')
    list_filter = ('is_used', 'created_at')
    search_fields = ('token', 'user__email')
    readonly_fields = ('token', 'created_at')
    fields = ('user', 'token', 'created_at', 'is_used')
    
    def is_valid_display(self, obj):
        return obj.is_valid()
    is_valid_display.boolean = True
    is_valid_display.short_description = 'Is valid'


@admin.register(PasswordResetToken)
class PasswordResetTokenAdmin(admin.ModelAdmin):
    list_display = ('token', 'user', 'created_at', 'is_used', 'is_valid_display')
    list_filter = ('is_used', 'created_at')
    search_fields = ('token', 'user__email')
    readonly_fields = ('token', 'created_at')
    fields = ('user', 'token', 'created_at', 'is_used')
    
    def is_valid_display(self, obj):
        return obj.is_valid()
    is_valid_display.boolean = True
    is_valid_display.short_description = 'Is valid'
