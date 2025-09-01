from django.contrib import messages
from django.shortcuts import redirect, get_object_or_404

from admin_panel.decorators.superuser import superuser_required
from users.models import User


@superuser_required
def user_delete_view(request, pk):
    user = get_object_or_404(User, pk=pk)
    try:
        user.delete()
    except Exception as e:
        print(e)
        messages.error(request, 'Profile does not exist!')
    else:
        messages.success(request, f'Profile {user.full_name} deleted!')
    return redirect('admin_panel:admin_user_list')
