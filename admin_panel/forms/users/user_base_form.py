from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator

from users.models import User


class BaseAdminUserForm(forms.ModelForm):
    telegram_chat_id = forms.IntegerField(
        required=False,
        label='Telegram Chat ID',
        validators=[
            MinValueValidator(1),
            MaxValueValidator(9999999999999999999)
        ],
        widget=forms.TextInput(attrs={'maxlength': '18'})
    )

    class Meta:
        model = User
        fields = [
            'email',
            'first_name',
            'last_name',
            'telegram_chat_id',
            'is_active',
            'is_staff',
            'is_superuser',
            'is_2fa_enabled',
        ]
        labels = {
            'is_superuser': 'Is Admin'
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

            if field_name in ('is_active', 'is_staff', 'is_superuser', 'is_2fa_enabled'):
                field.widget.attrs['class'] = 'form-check-input'

            if field.required:
                field.label += ' *'
