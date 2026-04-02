from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages

from users.forms.reset_password_form import ResetPasswordForm
from users.models import PasswordResetToken


def password_reset_view(request, token):
    token = get_object_or_404(PasswordResetToken, token=token)
    
    if token.is_used:
        messages.error(request, 'This verification link has already been used.')
        return redirect('users:login')
    
    if request.method == "POST":
        form = ResetPasswordForm(request.POST)
        if form.is_valid():
            user = token.user
            user.set_password(form.cleaned_data['new_password1'])
            user.save()
            token.use_token()
            messages.success(request, "Your password was successfully reset! Login to your account.")
            return redirect("users:login")
    else:
        form = ResetPasswordForm()
    
    context = {
        "form": form,
    }
    return render(request, "users/auth/password_reset.html", context)
