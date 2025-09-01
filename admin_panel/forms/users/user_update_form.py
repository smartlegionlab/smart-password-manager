from django import forms
from django.core.exceptions import ValidationError

from admin_panel.forms.users.user_base_form import BaseAdminUserForm


class AdminUserUpdateForm(BaseAdminUserForm):
    password = forms.CharField(
        widget=forms.PasswordInput,
        required=False,
        help_text="Leave blank to keep the current password."
    )

    class Meta(BaseAdminUserForm.Meta):
        fields = BaseAdminUserForm.Meta.fields + ['password', 'is_2fa_enabled',]
        labels = {
            **BaseAdminUserForm.Meta.labels,
            'is_2fa_enabled': 'Two-factor authentication',
        }

    def clean(self):
        cleaned_data = super().clean()
        is_2fa_enabled = cleaned_data.get('is_2fa_enabled')
        telegram_chat_id = cleaned_data.get('telegram_chat_id')

        if is_2fa_enabled and not telegram_chat_id:
            raise ValidationError('You must provide a Telegram Chat ID if two-factor authentication is enabled.')
        return cleaned_data
