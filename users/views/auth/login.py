from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render
from smartpasslib import SmartPasswordMaster, UrandomGenerator, HashGenerator

from core.utils.smart_redis.smart_redis_storage import RedisStorageManager
from users.forms.login_form import LoginForm
from users.models import User
from users.utils.auth.two_factor import send_2fa_code


def login_view(request):
    if request.user.is_authenticated:
        return redirect('users:user_detail')

    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            user = authenticate(request, email=email, password=password)

            if user is None:
                messages.error(request, 'Invalid email or password!')
                return render(request, 'users/auth/login_form.html', {'form': form})

            try:
                user = User.objects.get(id=user.id)
            except User.DoesNotExist:
                messages.error(request, 'User does not exist')
                return render(request, 'users/auth/login_form.html', {'form': form})

            if not user.is_active:
                messages.error(request, 'Account is not active! To activate, please contact your administrator.')
                return redirect('users:login')

            if user.is_2fa_enabled:

                if user.telegram_chat_id is None:
                    messages.error(request, 'Incorrect telegram id or telegram api error.')
                    return redirect('users:login')

                code = SmartPasswordMaster.generate_base_password(6)
                status = send_2fa_code(user, code)
                if status:
                    temp_data = UrandomGenerator.generate(30)
                    token = HashGenerator.generate(str(temp_data))
                    redis_storage = RedisStorageManager()

                    request.session.update({
                        "user_id": user.id,
                        "user_email": email,
                        "user_password": password
                    })
                    redis_storage.set_data(
                        uniq_key=f"{user.id}_2fa_code",
                        key="code",
                        value=code,
                        expiration=60
                    )
                    redis_storage.set_data(
                        uniq_key=f"{user.id}_2fa_token",
                        key="token",
                        value=token,
                        expiration=60
                    )
                    return redirect('users:auth_2fa', token=token)
                else:
                    messages.error(request, 'Incorrect telegram id or telegram api error.')
                    return redirect('users:login')

            login(request, user)
            messages.success(request, f'{user.full_name}, welcome!')
            return redirect('users:user_detail')

        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = LoginForm()

    return render(request, 'users/auth/login_form.html', {'form': form})
