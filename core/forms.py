from django import forms
from django.core.exceptions import ValidationError

from core.models import SiteConfig
from core.utils.checkers import check_phone_number


class SiteConfigForm(forms.ModelForm):
    class Meta:
        model = SiteConfig
        fields = ['name', 'description', 'email',]
        widgets = {
            'name': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Enter the name of the application'}),
            'description': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Enter a description'}),
        }
        labels = {
            'name': 'Application name',
            'description': 'Description of the application',
            'email': 'Email address',
        }

    def __init__(self, *args, **kwargs):
        super(SiteConfigForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            if self.fields[field_name].required:
                self.fields[field_name].label += ' *'

