from django import forms

from smart_pass_man.models import SmartPassword


class SmartPasswordForm(forms.ModelForm):
    secret_phrase = forms.CharField(max_length=255, label='Secret phrase')
    length = forms.IntegerField(
        min_value=12,
        max_value=100,
        label='Length',
        initial=15,
        widget=forms.NumberInput(attrs={'class': 'form-control', 'min': 12, 'max': 100})
    )

    class Meta:
        model = SmartPassword
        fields = ['login', 'secret_phrase', 'length',]
