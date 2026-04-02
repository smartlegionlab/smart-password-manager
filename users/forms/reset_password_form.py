from django import forms


class ResetPasswordForm(forms.Form):
    new_password1 = forms.CharField(
        label='New Password', 
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
    new_password2 = forms.CharField(
        label='Confirm new password', 
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )

    class Meta:
        fields = ('new_password1', 'new_password2')
    
    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('new_password1')
        password2 = cleaned_data.get('new_password2')
        
        if password1 and password2 and password1 != password2:
            self.add_error('new_password2', 'Passwords do not match.')
        
        return cleaned_data
