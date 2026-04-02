from django.contrib import messages
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.decorators.http import require_http_methods
from django.views.decorators.cache import never_cache
from django.core.cache import cache

from core.services.email_service import Email
from users.forms.password_forgot_form import PasswordForgotForm
from users.models import PasswordResetToken, User


@never_cache
def password_forgot_view(request):
    if request.method == "POST":
        form = PasswordForgotForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            
            cache_key = f'password_reset_attempts_{email.lower()}'
            attempts = cache.get(cache_key, 0)
            
            if attempts >= 3:
                messages.error(
                    request, 
                    'Too many reset attempts. Please wait an hour before trying again.'
                )
                return redirect('users:login')
            
            try:
                user = User.objects.get(email__iexact=email)
                
                token_obj = PasswordResetToken.create_token(user)
                
                reset_url = request.build_absolute_uri(
                    reverse('users:password_reset', kwargs={'token': token_obj.token})
                )
                
                Email.reset_password(
                    to=user.email,
                    username=user.first_name or user.username or user.email,
                    url=reset_url
                )
                
                cache.set(cache_key, attempts + 1, 3600)
                
            except User.DoesNotExist:
                pass
            
            messages.info(
                request, 
                f'If a user with this email exists, you will receive a link to reset your password.'
            )
    else:
        form = PasswordForgotForm()
    
    context = {
        'form': form,
    }
    return render(request, 'users/auth/password_forgot.html', context)


@require_http_methods(['GET', 'POST'])
def resend_password_reset_view(request):
    email = request.GET.get('email') or (request.POST.get('email') if request.method == 'POST' else None)
    
    if request.method == 'POST':
        email = request.POST.get('email')
    
    if not email:
        messages.error(request, 'Email address is required.')
        return redirect('users:login')
    
    cache_key = f'resend_password_reset_{email.lower()}'
    attempts = cache.get(cache_key, 0)
    
    if attempts >= 3:
        messages.error(
            request, 
            'Too many resend attempts. Please wait an hour before trying again.'
        )
        return redirect('users:login')
    
    try:
        user = User.objects.get(email__iexact=email)
        
        token_obj = PasswordResetToken.create_token(user)
        
        reset_url = request.build_absolute_uri(
            reverse('users:password_reset', kwargs={'token': token_obj.token})
        )
        
        Email.reset_password(
            to=user.email,
            username=user.first_name or user.username or user.email,
            url=reset_url
        )
        
        cache.set(cache_key, attempts + 1, 3600)
        
        messages.success(
            request, 
            f'Password reset link has been resent to {user.email}. '
            f'Please check your inbox and spam folder.'
        )
        
    except User.DoesNotExist:
        messages.success(
            request, 
            f'Password reset link has been resent to {user.email}. '
            f'Please check your inbox and spam folder.'
        )
    
    return redirect('users:password_forgot')
