from django.contrib import messages
from django.shortcuts import redirect, get_object_or_404

from admin_panel.decorators.superuser import superuser_required
from users.models import User


@superuser_required
def user_block_view(request, pk):
    user = get_object_or_404(User, pk=pk)
    user.is_active = not user.is_active
    user.save()

    if user.is_active:
        messages.success(request, f'Profile "{user.full_name}" is active!')
    else:
        messages.success(request, f'Profile "{user.full_name}" is inactive!')

    referer = request.META.get('HTTP_REFERER', 'admin_panel:admin-panel')
    return redirect(referer)
