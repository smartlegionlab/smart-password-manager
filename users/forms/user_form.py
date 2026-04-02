from django import forms

from users.forms.user_base_form import BaseUserForm


class UserEditForm(BaseUserForm):
    class Meta(BaseUserForm.Meta):
        fields = BaseUserForm.Meta.fields + ['is_2fa_enabled',]
        labels = {
            **BaseUserForm.Meta.labels,
            'is_2fa_enabled': 'Two-factor authentication',
        }
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }
