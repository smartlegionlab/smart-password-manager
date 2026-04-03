from django.contrib import messages
from django.db import IntegrityError
from django.shortcuts import render, redirect
from django.urls import reverse

from users.forms.register_form import RegisterForm
from users.models import EmailVerificationToken
from core.services.email_service import Email


def register_view(request):
    if request.user.is_authenticated:
        return redirect('users:user_detail')

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            try:
                user = form.save(commit=False)
                user.set_password(form.cleaned_data['password'])
                user.is_email_verified = False
                user.save()
                
                token_obj = EmailVerificationToken.create_token(user)
                
                verification_url = request.build_absolute_uri(
                    reverse('users:verify_email', kwargs={'token': token_obj.token})
                )
                
                Email.verification(
                    to=user.email,
                    username=user.first_name or user.username or user.email,
                    url=verification_url
                )
                
                messages.success(
                    request, 
                    f'{user.first_name}, registration successful! '
                    f'Please check your email ({user.email}) to verify your account.'
                )
                return redirect('users:login')
                
            except IntegrityError:
                messages.error(request, "This email is already registered.")
                return redirect('users:register')
    else:
        form = RegisterForm()
    
    context = {
        'form': form,
    }
    return render(request, 'users/auth/register_form.html', context)
