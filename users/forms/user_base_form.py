from django import forms

from users.models import User


class BaseUserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = [
            'email',
            'first_name',
            'last_name',
            'gender',
        ]
        labels = {
            'email': 'Email',
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'gender': 'Gender',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            if self.fields[field].required:
                self.fields[field].label += ' *'
