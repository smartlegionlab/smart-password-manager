from django.contrib import messages
from django.shortcuts import redirect

from admin_panel.decorators.superuser import superuser_required
from auth_logs.models import UserAuthLog


@superuser_required
def auth_logs_clear_view(request, pk):
    log_list =UserAuthLog.objects.filter(user_id=pk)
    try:
        log_list.delete()
    except Exception as e:
        print(e)
        messages.error(request, 'An error occurred while deleting user authentication history.')
    else:
        messages.success(request, 'Successfully deleted user authentication history.')
    return redirect('admin_panel:admin_user_auth_logs', pk=pk)
