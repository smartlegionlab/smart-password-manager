import json

from django.http import JsonResponse
from django.shortcuts import redirect, render
from smartpasslib import SmartPasswordMaster

from users.models import User


def password_reset_view(request):

    if request.user.is_authenticated:
        return redirect('users:user_detail')

    if request.method == 'POST':
        data = json.loads(request.body)
        email = data.get('email')
        telegram_id = data.get('telegram_id')
        user = User.objects.filter(email=email).first()
        temp_password = SmartPasswordMaster.generate_base_password(15)
        data = {
            'email': email,
            'profile': user,
        }
        if user is not None and all(data.values()):
            temp_password = SmartPasswordMaster.generate_base_password(15)
            status = True
            if status:
                user.set_password(temp_password)
                user.save()
                return JsonResponse({'success': True})
            else:
                return JsonResponse({'success': False, 'error': 'Incorrect telegram id or telegram api error.'})
        else:
            return JsonResponse({'success': False, 'error': 'Failed to reset password.'})
    context = {

    }
    return render(request, 'users/auth/password_reset_form.html', context)
