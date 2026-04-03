from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.views.decorators.cache import never_cache
from django.views.decorators.http import require_http_methods

from users.models import EmailVerificationToken, User
from core.services.email_service import Email


@never_cache
def verify_email_view(request, token):
    token_obj = get_object_or_404(EmailVerificationToken, token=token)
    
    if token_obj.is_used:
        messages.error(request, 'This verification link has already been used.')
        return redirect('users:login')
    
    if not token_obj.is_valid():
        messages.error(
            request, 
            'This verification link has expired. Please request a new verification email.'
        )
        token_obj.delete()
        return redirect('users:resend_verification')
    
    user = token_obj.user
    
    if user.is_email_verified:
        from django.core.cache import cache
        cache_key = f'resend_verification_{user.email.lower()}'
        cache.delete(cache_key)

        messages.info(request, 'Email already verified. You can log in now.')
        token_obj.use_token()
        return redirect('users:login')
    
    user.is_email_verified = True
    user.save()
    
    token_obj.use_token()
    
    messages.success(
        request, 
        f'Email verified successfully! You can now log in to your account.'
    )
    return redirect('users:login')


@require_http_methods(['GET', 'POST'])
def resend_verification_view(request):
    email = request.GET.get('email') or (request.POST.get('email') if request.method == 'POST' else None)
    
    if request.method == 'POST':
        email = request.POST.get('email')
    
    if not email:
        messages.error(request, 'Email address is required.')
        return redirect('users:login')
    
    from django.core.cache import cache
    cache_key = f'resend_verification_{email.lower()}'
    attempts = cache.get(cache_key, 0)
    
    if attempts >= 3:
        messages.error(
            request, 
            'Too many resend attempts. Please wait an hour before trying again.'
        )
        return redirect('users:login')
    
    try:
        user = User.objects.get(email__iexact=email)
        
        if user.is_email_verified:
            messages.info(request, 'This email is already verified. You can log in.')
            return redirect('users:login')
        
        token_obj = EmailVerificationToken.create_token(user)
        
        verification_url = request.build_absolute_uri(
            reverse('users:verify_email', kwargs={'token': token_obj.token})
        )
        
        Email.verification(
            to=user.email,
            username=user.first_name or user.username or user.email,
            url=verification_url
        )
        
        cache.set(cache_key, attempts + 1, 3600)
        
        messages.success(
            request, 
            f'Verification email has been resent to {user.email}. '
            f'Please check your inbox.'
        )
        
    except User.DoesNotExist:
        messages.error(request, 'No user found with this email address.')
    
    return redirect('users:login')
