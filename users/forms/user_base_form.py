from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator

from users.models import User


class BaseUserForm(forms.ModelForm):
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
        ]
        labels = {
            'email': 'Email',
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'telegram_chat_id': 'Telegram Chat ID',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            if self.fields[field].required:
                self.fields[field].label += ' *'
